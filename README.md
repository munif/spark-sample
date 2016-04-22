# spark-sample
Sample code for big data problems using Apache Spark (Python)

## Software Requirements
1. Python 2.7.x
2. [Apache Spark](http://spark.apache.org/)
3. `winutils.exe` (If you are running on Windows)

## Setup for Windows
Check the details [here](http://nishutayaltech.blogspot.co.id/2015/04/how-to-run-apache-spark-on-windows7-in.html).

1.  Set *environment variable* `SPARK_HOME` to spark's directory (where you extract the Apache Spark). For example: `D:\spark`. 
2.  Copy `winutils.exe` to the directory `D:\winutils\bin\`.
3.  Set *environment variable* `HADOOP_HOME` to `winutils.exe`'s directory (`D:\winutils\bin`).
