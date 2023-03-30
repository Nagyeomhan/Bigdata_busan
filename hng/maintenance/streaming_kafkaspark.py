### Q. Can I read real-time csv data which stored in Flask server with Kafka
### and preprocess it with Spark and store it as parquet file to HDFS
### and read it with HIVE?
### A. Yes, you can read real-time csv data stored in Flask server with Kafka,
### preprocess it with Spark, store it as parquet file to HDFS,
### and then read it with HIVE. Here is an example of how to do that:


## 1. Read the real-time csv data from Flask server using Kafka:
## In this example, we create a KafkaProducer instance
## and send the csv data to the 'csv-topic' topic.

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

def send_csv_to_kafka(csv_data):
    producer.send('csv-topic', csv_data.encode('utf-8'))


## 2. Consume the csv data using Spark and preprocess it:
## In this example, we use Spark to consume the csv data from the 'csv-topic' topic,
## preprocess the data, and store the preprocessed data in the 'processed_data' variable.

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('Preprocess CSV data').getOrCreate()

df = spark.read.format('csv').option('header', 'true').load('kafka://localhost:9092/csv-topic')
