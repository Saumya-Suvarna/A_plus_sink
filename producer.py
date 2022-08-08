import json

from kafka import KafkaProducer
from json import dumps


def producerData(data):
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                             value_serializer=lambda x:
                             dumps(x).encode('utf-8'))
    # data_payload = json.dumps(data)
    # data_str = str.encode(data_payload)
    producer.send('topicuser', value=data)
    # sleep(5)
