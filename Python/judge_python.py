import os
import json
import time
import re
from groq import Groq

ROOT_DIR = "."
OUTPUT_PATH = "./truth_inference_results.json"
API_CONFIG_PATH = "../config.json"
MODEL = "llama-3.1-8b-instant"
SLEEP_BETWEEN_CALLS = 1.2

with open(API_CONFIG_PATH, "r") as f:
    cfg = json.load(f)
client = Groq(api_key=cfg["api_key"])

def est_tokens(text):
    return max(1, int(len(text) / 4))

def clean_json_output(raw_output):
    cleaned = re.sub(r"<think>.*?</think>", "", raw_output, flags=re.DOTALL)
    cleaned = cleaned.strip()
    start = cleaned.find("{")
    if start == -1:
        return cleaned.strip()
    depth = 0
    for i, ch in enumerate(cleaned[start:], start=start):
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return cleaned[start:i + 1].strip()
    return cleaned[start:].strip()

items = []
for root, _, files in os.walk(ROOT_DIR):
    for fname in files:
        if fname.endswith(".py"):
            full_path = os.path.join(root, fname)
            try:
                with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                    code = f.read()
                rel_path = os.path.relpath(full_path, ROOT_DIR)
                parts = rel_path.split(os.sep)
                if len(parts) >= 2:
                    algo_name = parts[0]
                    model_name = parts[1]
                else:
                    algo_name = "unknown_algo"
                    model_name = "unknown_model"
                uid = f"{algo_name}||{model_name}"
                items.append({
                    "algo": algo_name,
                    "model": model_name,
                    "code": code,
                    "id": uid
                })
            except Exception as e:
                print(f"Couldn't read {full_path}: {e}")

if not items:
    raise SystemExit("No .py submissions found under ROOT_DIR.")

print(f"Found {len(items)} total Python submissions.")

persona_judge = (
    "You are a highly analytical and impartial expert judge specialized in Python programming. "
    "Your goal is to perform Truth Inference in an adversarial context. "
    "You must analyze multiple Python implementations of the same task and classify each one "
    "based on factual correctness and plausibility of their behavior."
)

def build_prompt_for_submission(item):
    verdicts_template = f'"{item["id"]}": "<one of correct | plausible | incorrect | invalid>"'
    prompt = f"""Persona: {persona_judge}

You will be given one Python source code. Evaluate it independently.

Classify it into exactly one of the following categories:
- "correct": fully functional and logically correct.
- "plausible": mostly correct but with minor flaws.
- "incorrect": significant logical or implementation errors.
- "invalid": fails to compile or incomplete.

Return ONLY a valid JSON, with no commentary, no explanation, no repeated JSONs, and no text before or after it.

Use exactly this format:

{{
  "verdicts": {{
    {verdicts_template}
  }},
  "summary": "<brief justification>"
}}

### TASK: Please write your best implementation of {item['algo']} in Python.
### SUBMISSION ID: {item['id']}
# model: {item['model']}
{item['code']}
"""
    return prompt

partial_outputs = []

for i, item in enumerate(items, start=1):
    prompt = build_prompt_for_submission(item)
    print(f"Processing {i}/{len(items)}: {item['id']} (~{est_tokens(prompt)} tokens)...")
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            max_completion_tokens=3072,
        )
        raw = response.choices[0].message.content
        cleaned = clean_json_output(raw)
        try:
            parsed = json.loads(cleaned)
            partial_outputs.append(parsed)
            print("Parsed successfully.")
        except Exception as e:
            print(f"JSON parse error: {e}")
            partial_outputs.append({"error": "parse_failed", "raw": cleaned})
    except Exception as e:
        print(f"API error on {item['id']}: {e}")
        partial_outputs.append({"error": "api_error", "message": str(e)})
    time.sleep(SLEEP_BETWEEN_CALLS)

final_results = {}

for out in partial_outputs:
    if "verdicts" in out and isinstance(out["verdicts"], dict):
        for id_key, cat in out["verdicts"].items():
            algo, model = id_key.split("||", 1) if "||" in id_key else (id_key, "unknown")
            final_results.setdefault(algo, {"verdicts": {}, "summaries": []})
            final_results[algo]["verdicts"][model] = cat
        if "summary" in out:
            for id_key in out["verdicts"].keys():
                algo = id_key.split("||", 1)[0]
                final_results[algo]["summaries"].append(out.get("summary", ""))
    else:
        final_results.setdefault("_errors", []).append(out)

for algo, data in final_results.items():
    if algo == "_errors":
        continue
    summary = " ".join([s for s in data.get("summaries", []) if s]) or "No summary available."
    final_results[algo]["summary"] = summary
    final_results[algo].pop("summaries", None)

output_list = [
    {algo: {"verdicts": data["verdicts"], "summary": data["summary"]}}
    for algo, data in final_results.items() if algo != "_errors"
]
if "_errors" in final_results:
    output_list.append({"_errors": final_results["_errors"]})

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(output_list, f, indent=2, ensure_ascii=False)

print(f"Aggregated truth-inference results saved to: {OUTPUT_PATH}")
