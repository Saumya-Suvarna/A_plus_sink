import json

from kafka import KafkaProducer
from json import dumps


def producerData(data):
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                             value_serializer=lambda x:
                             dumps(x).encode('utf-8'))
    producer.send('topicuser', value=data)

