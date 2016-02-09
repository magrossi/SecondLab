HADOOP_CLASSPATH="$(hadoop classpath)"
javac -classpath $HADOOP_CLASSPATH WordCount.java
jar cf wc.jar WordCount*.class