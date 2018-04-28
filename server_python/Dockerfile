FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code2
WORKDIR /code2
ADD requirements.txt /code2/
RUN pip3 install protobuf
RUN pip install psycopg2
ADD . /code2/
