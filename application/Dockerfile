FROM ubuntu/python:3.12-24.04_stable

ADD log_generator.py /application/
ADD get-pip.py /application/
ADD get-confluent-kafka.py /application/

WORKDIR /application/

RUN ["python3", "get-pip.py"]
RUN ["python3", "get-confluent-kafka.py"]
ENTRYPOINT ["python3", "log_generator.py"]