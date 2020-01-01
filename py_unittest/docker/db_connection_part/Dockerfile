FROM python:3.7

FROM google/cloud-sdk:274.0.1

RUN apt-get update && \
  apt-get install -y vim gzip wget 

COPY ./for-my-study-bq.json /tmp/for-my-study-bq.json
RUN gcloud auth activate-service-account --key-file /tmp/for-my-study-bq.json && \
  rm /tmp/for-my-study-bq.json
