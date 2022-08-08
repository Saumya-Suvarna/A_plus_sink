from kafka import KafkaConsumer
from json import loads

import models


def consumerData():
    consumer = KafkaConsumer(
        'post',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='latest',
        enable_auto_commit=True,
        auto_commit_interval_ms=1000,
        value_deserializer=lambda x: loads(x.decode('utf-8')))
    for message in consumer:
        postData = message.value

        print("post data")
        print(postData)
        models.Post.create(
            user=postData["user"],
            content=postData["content"],
			timing = postData["timing"]
            )

        print('Session posted successfully', postData["user"])


if __name__ == '__main__':
    consumerData()
