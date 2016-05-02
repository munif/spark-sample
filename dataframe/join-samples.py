from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext

# Function for printing each element in RDD
def println(x):
    print x

# Function for transforming the tweet
def transformTweets(line):
    # Data sample: "1, aku suka kamu". Splitted to data[0] = 1, data[1] = "aku suka kamu"
    data = line.split(",")
    id = data[0]
    tweet = data[1]
    
    # Map each word to id using builtin 'map' function
    # The results are [1, "aku"], [1, "suka"], [1, "kamu"]
    result = map((lambda x: [id, x]), tweet.split(" ")) # input 'x' from splitted string of tweet
    return result


# 1. Define the context
conf = SparkConf().setMaster("local").setAppName("Join Samples")
sc = SparkContext(conf = conf)
sqlContext = SQLContext(sc)

# 2. Load and transform sentiment
# 2.1 Load the sentiment
sentiment = sc.textFile("sentiment.csv")
sentiment.cache()
sentiment.collect()
print 'Sentiment data:'
sentiment.foreach(println)
print '\n'

# 2.2 Transforming the sentiment
sentimentMap = sentiment.map(lambda x: x.split(' '))
sentimentMap.cache()
sentimentMap.collect()
print 'Sentiment map data:'
sentimentMap.foreach(println)
print '\n'

# 3. Load and transform tweet
# 3.1 Load the tweets
tweets = sc.textFile("tweets.csv")
tweets.cache()
tweets.collect()
print 'Tweet data:'
tweets.foreach(println)
print '\n'

# 3.2 Transforming the tweet
# 3.2.1 using map -> array of array
tweetsMap = tweets.map(transformTweets)
tweetsMap.cache()
tweetsMap.collect()
print 'Tweet mapdata'
tweetsMap.foreach(println)
print '\n'

# 3.2.2 using flatMap -> flattened array (this is what we want)
tweetsFlatMap = tweets.flatMap(transformTweets)
tweetsFlatMap.cache()
tweetsFlatMap.collect()
print 'Tweet flatMap data'
tweetsFlatMap.foreach(println)
print '\n'

# 4. Convert to data frame
# 4.1 Convert sentimentMap
sentimentDf = sqlContext.createDataFrame(sentimentMap, ["word", "type", "sentiment"])
sentimentDf.cache()
sentimentDf.show()

# 4.2 Convert tweetsFlatMap
tweetsDf = sqlContext.createDataFrame(tweetsFlatMap, ["tweet_id", "word"])
tweetsDf.cache()
tweetsDf.show()

# 5. Join the dataframe
joinedDf = tweetsDf.join(sentimentDf, tweetsDf.word == sentimentDf.word)
joinedDf.cache()
joinedDf.show()
