# -*- coding: utf-8 -*-
#Load the CSV file into a RDD

import sys;
reload(sys);
sys.setdefaultencoding("utf8")

from pyspark.sql import SQLContext
from pyspark import SparkConf, SparkContext
import collections

# Function for printing each element in RDD
def println(x):
    print x
    
def TransformToVector(inputStr):
    attList=inputStr.split(",")
    smsType= 0.0 if attList[0] == "ham" else 1.0
    return [smsType, attList[1]]


conf = SparkConf().setMaster("local").setAppName("Spam Filtering")
sc = SparkContext(conf = conf)

sqlContext = SQLContext(sc)

smsData = sc.textFile("SMSSpamCollection.csv",2)
smsData.cache()
smsData.collect()

smsXformed=smsData.map(TransformToVector)

smsDf= sqlContext.createDataFrame(smsXformed,
                          ["label","message"])
smsDf.cache()
smsDf.select("label","message").show()

##Split training and testing
(trainingData, testData) = smsDf.randomSplit([0.9, 0.1])
print trainingData.count()
print testData.count()
testData.collect()


#Setup pipeline
from pyspark.ml.classification import NaiveBayes, NaiveBayesModel
from pyspark.ml import Pipeline
from pyspark.ml.feature import HashingTF, Tokenizer
from pyspark.ml.feature import IDF

tokenizer = Tokenizer(inputCol="message", outputCol="words")
hashingTF = HashingTF(inputCol=tokenizer.getOutputCol(), \
        outputCol="tempfeatures")
idf=IDF(inputCol=hashingTF.getOutputCol(), outputCol="features")
nbClassifier=NaiveBayes()

pipeline = Pipeline(stages=[tokenizer, hashingTF, \
                idf, nbClassifier])

nbModel=pipeline.fit(trainingData)

prediction=nbModel.transform(testData)

#prediction.where(prediction.prediction == 1.0).show()

prediction.groupBy("label","prediction").count().show()
