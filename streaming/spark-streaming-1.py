#Initiate Spark context. Once this is done all other applications can run
from pyspark import SparkContext
from pyspark import SparkConf

# Optionally configure Spark Settings
conf=SparkConf()
conf.set("spark.executor.memory", "1g")
conf.set("spark.cores.max", "4")

conf.setAppName("Spark Streaming Examples")

## Initialize SparkContext. Run only once. Otherwise you get multiple 
#Context Error.
#for streaming, create a spark context with 2 threads.
sc = SparkContext('local[4]', conf=conf)

from pyspark.streaming import StreamingContext

#............................................................................
##   Streaming with TCP/IP data
#............................................................................

#Create streaming context with latency of 1
streamContext = StreamingContext(sc, 3)

totalLines=0
lines = streamContext.socketTextStream("localhost", 9000)


#Word count within RDD    
words = lines.flatMap(lambda line: line.split(" "))
pairs = words.map(lambda word: (word, 1))
wordCounts = pairs.reduceByKey(lambda x, y: x + y)
wordCounts.pprint(5)

#Count lines
totalLines=0
linesCount=0
def computeMetrics(rdd):
    global totalLines
    global linesCount
    linesCount=rdd.count()
    totalLines+=linesCount
    print rdd.collect()
    print "Lines in RDD :", linesCount," Total Lines:",totalLines

lines.foreachRDD(computeMetrics)

#Compute window metrics
def windowMetrics(rdd):
    print "Window RDD size:", rdd.count()
    
windowedRDD=lines.window(6,3)
windowedRDD.foreachRDD(windowMetrics)

streamContext.start()
#streamContext.stop()
streamContext.awaitTermination()
print "Overall lines :", totalLines