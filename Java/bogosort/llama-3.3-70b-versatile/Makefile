compile:
	javac -d . Llama_3_3_70b_versatile.java

measure:
	sudo modprobe msr
	sudo ../RAPL/main "/usr/lib/jvm/java-11-openjdk-amd64/bin/java -cp . Llama_3_3_70b_versatile 10" Java Llama_3_3_70b_versatile

run:
	/usr/lib/jvm/java-11-openjdk-amd64/bin/java -cp . Llama_3_3_70b_versatile 10

mem:
	/usr/bin/time -v /usr/bin/java -Xmx10m -cp . Llama_3_3_70b_versatile 10

valgrind:
	valgrind --tool=massif --stacks=yes /usr/bin/java -Xmx10m -cp . Llama_3_3_70b_versatile 10
