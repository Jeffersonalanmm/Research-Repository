compile:
	javac -d . theAlgorithms.java

measure:
	sudo ../RAPL/main "/usr/lib/jvm/java-11-openjdk-amd64/bin/java -cp . com.avl.theAlgorithms.theAlgorithms 1000" Java theAlgorithms

run:
	/usr/lib/jvm/java-11-openjdk-amd64/bin/java -cp . com.avl.theAlgorithms.theAlgorithms 1000

mem:
	/usr/bin/time -v /usr/bin/java -Xmx10m -cp . com.avl.theAlgorithms.theAlgorithms 1000

valgrind:
	valgrind --tool=massif --stacks=yes /usr/bin/java -Xmx10m -cp . com.avl.theAlgorithms.theAlgorithms 1000
