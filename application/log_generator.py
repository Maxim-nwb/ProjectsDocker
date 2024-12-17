#!/usr/bin/env python
# coding: utf-8


import time
from confluent_kafka import Producer
import json
import random 


log_type_list = ["ERROR", "INFO", "WARNING"]
error_code_list = ["404", "400", "403"]
event_type_list = ["CREATE", "DELITE", "SAVE", "OVERRIDE", "APPEND"]
event_status_list = ["DONE", "CANCEL"]

class LogOne():
    def __init__(self):
        self.application = 1
        self.timestamp = time.time()
        self.log_type = random.choice(log_type_list)
        self.error_code = None
        self.count_operations = random.randint(1, 100)
        self.type_work_counts = random.randint(1, 20)
        self._set_error_code()
    
    def _set_error_code(self):
        if self.log_type == "ERROR": 
            self.error_code = random.choice(error_code_list)

class LogTwo():
    def __init__(self):
        self.application = 2
        self.timestamp = time.time()
        self.log_type = random.choice(log_type_list)
        self.error_code = None
        self.event_id = random.randint(1, 50)
        self.event_name = random.choice(event_type_list)
        self.event_status = random.choice(event_status_list)
        self._set_error_code()

    def _set_error_code(self):
        if self.log_type == "ERROR": 
            self.error_code = random.choice(error_code_list)

class LogThree():
    def __init__(self):
        self.application = 3
        self.timestamp = time.time()
        self.log_type = random.choice(log_type_list)
        self.error_code = None
        self.user_id = random.randint(100, 999)
        self.user_position_id = random.randint(1,3)
        self._set_error_code()

    def _set_error_code(self):
        if self.log_type == "ERROR": 
            self.error_code = random.choice(error_code_list)


config = {
    'bootstrap.servers': 'kafka:29092',
    'auto.offset.reset': 'earliest'
}


producer = Producer(config)

def send_message(topic, message):
    producer.produce(topic, value=message)
    producer.flush()


def LogGerator(app_num):

    match app_num:
        case 1:
            return LogOne()
        case 2:
            return LogTwo()
        case 3:
            return LogThree()


while True:

    LogsCount = random.randint(1, 10)

    for i in range(LogsCount):
        
        application = random.randint(1, 3)

        log = LogGerator(application)

        send_message('logs', json.dumps(vars(log)))

    time.sleep(random.randint(3, 10))
    
    