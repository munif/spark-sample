# spark-sample
Sample code for big data problems using Apache Spark (Python)

## Software Requirements
1. Python 2.7.x
2. [Apache Spark](http://spark.apache.org/)
3. `winutils.exe` (If you are running on Windows)
4. [Enthought Canopy](https://www.enthought.com/products/canopy/)

## Setup for Windows
Check the details [here](http://nishutayaltech.blogspot.co.id/2015/04/how-to-run-apache-spark-on-windows7-in.html).

1.  Set *environment variable* `SPARK_HOME` to Spark's directory (where you extract the Apache Spark). For example: `D:\spark`. 
    Make sure that your Spark directory structure is like this.
    ![Spark's directory](https://raw.githubusercontent.com/munif/spark-sample/master/screenshots/spark-home.png "Spark's Directory")
2.  Copy `winutils.exe` to the directory `D:\winutils\bin\`.
3.  Set *environment variable* `HADOOP_HOME` to `winutils.exe`'s directory (`D:\winutils\bin`).
