# pull official base imgae
FROM python:3.10-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITECODE 1
ENV PYTHONEUNBUFFERED 1

COPY . /usr/src/app
# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt