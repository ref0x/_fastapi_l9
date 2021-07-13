FROM python:3.9.5-alpine3.13
LABEL maintainer="kakbari
RUN apk update && apk upgrade && apk add bash

COPY . ./app

RUN ["mkdir", "/a_directory"]
# CMD ["python", "./my_script.py"]

