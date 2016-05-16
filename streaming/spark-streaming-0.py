#Initiate Spark context. Once this is done all other applications can run
from pyspark import SparkContext
from pyspark import SparkConf

# Optionally configure Spark Settings
conf=SparkConf()
conf.set("spark.executor.memory", "1g")
conf.set("spark.cores.max", "2")

conf.setAppName("Spark Streaming Sample")

## Initialize SparkContext. Run only once. Otherwise you get multiple 
#Context Error.
#for streaming, create a spark context with 4 threads.
sc = SparkContext('local[4]', conf=conf)

from pyspark.streaming import StreamingContext

#............................................................................
##   Streaming with simple data
#............................................................................

vc = [[-0.1, -0.2], [0.1, 0.3], [1.1, 1.5], [0.9, 0.9]]
dvc = [sc.parallelize(i, 1) for i in vc]
ssc = StreamingContext(sc, 2)
input_stream = ssc.queueStream(dvc)

def get_output(rdd):
    print(rdd.collect())
    
#input_stream.foreachRDD(get_output)
input_stream.pprint()

ssc.start()
ssc.awaitTermination()
