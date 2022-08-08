from kafka import KafkaConsumer
from json import loads

import models


def consumerData():
    consumer = KafkaConsumer(
        'topicuser',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='latest',
        enable_auto_commit=True,
        auto_commit_interval_ms=1000,
        value_deserializer=lambda x: loads(x.decode('utf-8')))
    for message in consumer:
        userData = message.value

        print("user data")
        print(userData)

        models.User.create_user(
            username=userData["username"],
            email=userData["email"],
            password=userData["password"],
            current_role=userData["curent_role"],
            current_company=userData["current_company"],
            first_name=userData["first_name"],
            last_name=userData["last_name"],
            skills=userData["skills"],
            description=userData["description"]
        )
        print('registration successful-', userData)


if __name__ == '__main__':
    consumerData()
