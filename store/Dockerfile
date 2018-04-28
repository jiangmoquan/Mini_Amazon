FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN apt-get update && apt-get install -yq --no-install-recommends nodejs npm && apt-get clean
RUN npm install -g bower
RUN pip install -r requirements.txt
ADD . /code/
