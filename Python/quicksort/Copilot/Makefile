compile:
	cp Copilot.python3 Copilot.py

measure:
	sudo modprobe msr
	sudo ../RAPL/main "python3 -OO Copilot.py 1000" Python Copilot

run:
	python3 -OO Copilot.py 1000

mem:
	/usr/bin/time -v python3 -OO Copilot.py 1000

valgrind:
	valgrind --tool=massif --stacks=yes python3 -OO Copilot.py 10