compile:
	/usr/bin/gcc -pipe -Wall -O3 -fomit-frame-pointer -march=native -fopenmp -D_FILE_OFFSET_BITS=64 -I/usr/include/apr-1.0 rosetta.c -o rosetta_run -lapr-1 -lgomp -lm
	
measure:
	sudo modprobe msr
	sudo ../RAPL/main "./rosetta_run 1000" C Rosetta

run:
	./rosetta_run 1000

mem:
	/usr/bin/time -v ./rosetta_run 1000