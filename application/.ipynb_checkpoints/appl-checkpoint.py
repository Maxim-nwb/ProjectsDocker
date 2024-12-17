#!/usr/bin/env python
# coding: utf-8


import time
from confluent_kafka import Producer
import json 


class TestCl(): {
    def __init__(self, count):
    self.t = "Hello Kafka World!"
    self.count = count

}

config = {
    'bootstrap.servers': 'kafka:29092',
    'auto.offset.reset': 'earliest'
}


producer = Producer(config)

def send_message(topic, message):
    producer.produce(topic, value=message)
    producer.flush()

n = 0

while True:
    k = TestCl(n)
    send_message('test', json.dumps(k))
    time.sleep(3)
    n +=1
    