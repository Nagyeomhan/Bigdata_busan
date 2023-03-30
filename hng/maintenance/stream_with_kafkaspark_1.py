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

# preprocess the data
processed_data = ...


## 3. Store the preprocessed data in parquet format in HDFS:
## Replace values in < > with the appropriate values for your Hadoop Cluster

# write data in parquet format to HDFS
processed_data.write.mode('overwrite').parquet('hdfs://<HDFS_NAME_NODE>:<HDFS_PORT>/<HDFS_PATH>/<FILENAME>.parquet')


## 4. Create an external table in HIVE to access the data stored in parquet format:
## Replace values in < > with the appropriate values for your Hadoop Cluster

CREATE EXTERNAL TABLE <TABLE_NAME> (
    <COLUMN_1> <DATA_TYPE_1>,
    <COLUMN_2> <DATA_TYPE_2>,
    ...
)

STORED AS PARQUET
LOCATION 'hdfs://<HDFS_NAME_NODE>:<HDFS_PORT>/<HDFS_PATH>'


## 5. Query the data using HIVE:
## Replace values in < > with the appropriate values for your use case

SELECT * FROM <TABLE_NAME> WHERE <CONDITION>;


### By reading the real-time csv data with Kafka and storing the preprocessed data in parquet format in HDFS,
### you can benefit from the efficient storage and compression of columnar data
### and by using HIVE, you can query the data using SQL-like syntax