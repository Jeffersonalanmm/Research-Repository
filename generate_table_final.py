import pandas as pd
import json
import os
import re
import numpy as np
from typing import Dict, Any, List

def extrair_veredictos_brutos_do_arquivo(file_path: str) -> List[Dict[str, str]]:
    content_raw = ""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content_raw = f.read()
        
        data = json.loads(content_raw)

    except json.JSONDecodeError as e:
        print(f"WARNING: JSON decoding error in file {file_path}: {e}")
        try:
            content_cleaned = re.sub(r',\s*([\]\}])', r'\1', content_raw)
            content_cleaned = content_cleaned.replace("'", '"')
            data = json.loads(content_cleaned)
                
        except Exception as e_inner:
            print(f"Error during recovery attempt for {file_path}: {e_inner}")
            return []

    except Exception as e:
        print(f"Unexpected error processing file {file_path}: {e}")
        return []
        
    veredictos_brutos = []
    if isinstance(data, list):
        for item in data: 
            if isinstance(item, dict):
                for task_name in item:
                    if isinstance(item[task_name], dict) and 'verdicts' in item[task_name]:
                        verdicts = item[task_name]['verdicts']
                        for model_name_raw, verdict in verdicts.items():
                            veredictos_brutos.append({
                                'model_raw': model_name_raw, 
                                'verdict': verdict
                            })
                
    return veredictos_brutos

arquivos_para_processar = [
    {'path': 'table/gpt-oss-120b/java.json', 'linguagem': 'Java'},
    {'path': 'table/gpt-oss-120b/python.json', 'linguagem': 'Python'},
    {'path': 'table/gpt-oss-120b/c.json', 'linguagem': 'C'},
    {'path': 'table/kimi-k2-instruct-0905/java.json', 'linguagem': 'Java'},
    {'path': 'table/kimi-k2-instruct-0905/python.json', 'linguagem': 'Python'},
    {'path': 'table/kimi-k2-instruct-0905/c.json', 'linguagem': 'C'},
    {'path': 'table/llama-3.1-8b-instant/java.json', 'linguagem': 'Java'},
    {'path': 'table/llama-3.1-8b-instant/python.json', 'linguagem': 'Python'},
    {'path': 'table/llama-3.1-8b-instant/c.json', 'linguagem': 'C'},
    {'path': 'table/llama-4-maverick-17b-128e-instruct/java.json', 'linguagem': 'Java'},
    {'path': 'table/llama-4-maverick-17b-128e-instruct/python.json', 'linguagem': 'Python'},
    {'path': 'table/llama-4-maverick-17b-128e-instruct/c.json', 'linguagem': 'C'},
    {'path': 'table/qwen3-32b/java.json', 'linguagem': 'Java'},
    {'path': 'table/qwen3-32b/python.json', 'linguagem': 'Python'},
    {'path': 'table/qwen3-32b/c.json', 'linguagem': 'C'},
]

mapeamento_nomes = {
    'deepseek-r1-distill-llama-70b': 'Deepseek-70b',
    'gemma2-9b-it': 'Gemma2-9b-it',
    'llama-3.2-90b-vision-preview': 'Llama-3.2-90b',
    'llama-3.3-70b-versatile': 'Llama-3.3-70b',
    'mixtral-8x7b-32768': 'Mixtral-8x7b',
    'mixtral-8x7x-32768': 'Mixtral-8x7b', 
    'rosetta': 'Rosetta',
    'thealgorithms': 'TheAlgorithms',
    'qwen3-32b': 'Qwen32b',
    'gpt-oss-120b': 'GPT120b',
    'llama-4-maverick-17b-128e-instruct': 'Llama-Maverick',
    'amazonq': 'AmazonQ',
    'chatgpt': 'ChatGPT', 
    'gemini': 'Gemini',
    'blackbox': 'BlackBox',
    'codeium': 'Codeium',
    'copilot': 'Copilot',
    'kimi-k2-instruct-0905': 'Kimi',
    'llama-3.1-8b-instant': 'Llama-3.1-8b-ins',
    'rapl': 'RAPL'
}

dados_brutos_completos = []

for config in arquivos_para_processar:
    file_path = config['path']
    linguagem = config['linguagem']
    
    if not os.path.exists(file_path):
        file_path_docx = file_path.replace('.json', '.docx')
        if os.path.exists(file_path_docx):
             file_path = file_path_docx
        else:
            print(f"WARNING: File not found: {config['path']}")
            continue

    veredictos_brutos = extrair_veredictos_brutos_do_arquivo(file_path)
    
    for v in veredictos_brutos:
        model_raw = v['model_raw']
        verdict = v['verdict'].lower()
        
        model_name = mapeamento_nomes.get(model_raw.lower(), model_raw)

        if model_name.lower() == 'rapl':
            continue
        
        if verdict in ['correct', 'plausible', 'incorrect', 'invalid']:
            dados_brutos_completos.append({
                'Modelo': model_name, 
                'Linguagem': linguagem, 
                'Métrica': verdict.capitalize() 
            })

if not dados_brutos_completos:
    print("No data was processed. Check file paths and JSON format.")
    exit()

df_raw = pd.DataFrame(dados_brutos_completos)

df_counts = df_raw.groupby(['Modelo', 'Linguagem', 'Métrica']).size().reset_index(name='Valor')

ordem_metricas = ['Correct', 'Plausible', 'Incorrect', 'Invalid']
ordem_linguagens = ['Java', 'Python', 'C']

df_final_long = df_counts[df_counts['Métrica'].isin(ordem_metricas)]

df_pivot = df_final_long.pivot_table(
    index=['Modelo', 'Métrica'],
    columns='Linguagem',
    values='Valor',
    aggfunc='first'
).reset_index()

df_pivot['Métrica'] = pd.Categorical(df_pivot['Métrica'], categories=ordem_metricas, ordered=True)
df_pivot = df_pivot.sort_values(['Modelo', 'Métrica']).reset_index(drop=True)

cols_to_keep = ['Modelo', 'Métrica'] + [col for col in ordem_linguagens if col in df_pivot.columns]
df_pivot = df_pivot[cols_to_keep]

df_pivot_counts = df_counts.pivot_table(
    index=['Linguagem'], 
    columns='Métrica', 
    values='Valor',
    aggfunc='sum', 
    fill_value=0
)

for col in ['Correct', 'Plausible', 'Incorrect', 'Invalid']:
    if col not in df_pivot_counts.columns:
        df_pivot_counts[col] = 0

df_totals_T = df_pivot_counts[ordem_metricas].transpose().reset_index()
df_totals_T.rename(columns={'index': 'Métrica'}, inplace=True)
df_totals_T['Modelo'] = 'TOTAL'
df_total_rows = df_totals_T[['Modelo', 'Métrica'] + [col for col in ordem_linguagens if col in df_totals_T.columns]]

df_pivot_counts['Total'] = df_pivot_counts[ordem_metricas].sum(axis=1)
df_pivot_counts['PFC_Value'] = (
    (df_pivot_counts['Correct'] + df_pivot_counts['Plausible']) / df_pivot_counts['Total'] * 100
).fillna(0).round(1)

pfc_row = {'Modelo': 'PFC', 'Métrica': ''} 
for lang in ordem_linguagens:
    if lang in df_pivot_counts.index:
        pfc_row[lang] = df_pivot_counts.loc[lang, 'PFC_Value']
    else:
        pfc_row[lang] = '-' 

df_pfc_row = pd.DataFrame([pfc_row])

df_pivot.rename(columns={'Métrica': ''}, inplace=True)
df_total_rows.rename(columns={'Métrica': ''}, inplace=True)

df_final_table = pd.concat([df_pivot, df_total_rows, df_pfc_row], ignore_index=True)

cols_to_fill = [col for col in ordem_linguagens if col in df_final_table.columns]
for col in cols_to_fill:
    df_final_table[col] = df_final_table[col].astype(object).replace({np.nan: '-'})

for col in cols_to_fill:
    df_final_table[col] = df_final_table.apply(
        lambda row: f"{float(row[col]):.1f}" 
        if row['Modelo'] == 'PFC' and row[col] != '-' else (
            int(row[col]) if row[col] != '-' else row[col]
        ), 
        axis=1
    )

def remove_duplicate_modelo(df):
    current_model = None
    new_modelo_list = []
    for model in df['Modelo']:
        if model == current_model:
            new_modelo_list.append('')
        elif model == 'PFC' or model == 'TOTAL': 
            new_modelo_list.append(model) 
            current_model = model 
        else:
            new_modelo_list.append(model)
            current_model = model
    df['Modelo'] = new_modelo_list
    return df

df_final_table = remove_duplicate_modelo(df_final_table.copy())

print("\n--- Final Table Generated (V9 - With TOTAL Row) ---")
try:
    tabela_markdown = df_final_table.to_markdown(index=False, stralign='center', numalign='center')
except ImportError:
    print("WARNING: Missing dependency 'tabulate' (pip install tabulate). Using standard to_markdown.")
    tabela_markdown = df_final_table.to_markdown(index=False)
    
print(tabela_markdown)

try:
    df_final_table.to_csv('final_results.csv', index=False, encoding='utf-8')
    print("\n[+] Table successfully saved to 'final_results.csv'")
except Exception as e:
    print(f"\n[-] Error saving CSV: {e}")