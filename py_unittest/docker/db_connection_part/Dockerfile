FROM python:3.7

RUN pip install \
  dataset mysqlclient google-cloud-bigquery

RUN apt-get update && \
  apt-get install -y vim gzip wget
#  libmysqlclient-dev 

#COPY ./for-my-study-bq.json /tmp/for-my-study-bq.json
#RUN gcloud auth activate-service-account --key-file /tmp/for-my-study-bq.json && \
#  rm /tmp/for-my-study-bq.json
