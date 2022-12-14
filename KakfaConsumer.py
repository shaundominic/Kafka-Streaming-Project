from kafka import KafkaConsumer
from time import sleep
from json import dumps,loads
import json
from s3fs import S3FileSytem

consumer=KafkaConsumer('demo_test',
bootstrap_servers=['65.21.21.43:9092'],
value_deserializer=lambda x:loads(x.decode('utf-8')))

s3=S3FileSytem()

for count, i in enumerate(consumer):
  with s3.open('s3://kafka-bucket/stock_market_{}.json'.format(count),'w') as file:
    json.dump(i.value, file)