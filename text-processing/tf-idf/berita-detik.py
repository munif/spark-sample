from pyspark import SparkConf, SparkContext
from pyspark.mllib.feature import HashingTF
from pyspark.mllib.feature import IDF

# Function for printing each element in RDD
def println(x):
    print x

# Boilerplate Spark stuff:
conf = SparkConf().setMaster("local[*]").setAppName("SparkTFIDF")
sc = SparkContext(conf = conf)

# Load documents (one per line).
rawData = sc.textFile("doc-sample.csv")
fields = rawData.map(lambda x: x.split(","))
documents = fields.map(lambda x: x[1].split(" "))

documentId = fields.map(lambda x: x[0])

# Creating Hash table and TF table
hashingTF = HashingTF(100000)
tf = hashingTF.transform(documents)

# Creating idf
tf.cache()
idf = IDF(minDocFreq=1).fit(tf)

# Calculate TF/IDF
tfidf = idf.transform(tf)

# Keyword yang akan dicari diubah ke Hash value <- Hash table di atas

keywordTF = hashingTF.transform(["Bule"])
keywordHashValue = int(keywordTF.indices[0])

# Temukan relevansinya dengan tabel tf-idf yang sudah dibuat
keywordRelevance = tfidf.map(lambda x: x[keywordHashValue])

zippedResults = keywordRelevance.zip(documentId)

print "Best document for keywords is:"
print zippedResults.max()