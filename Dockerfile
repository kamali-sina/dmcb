# base image  

FROM python:3.8-slim-buster
ENV DockerHOME=/home/app/webapp
RUN mkdir -p $DockerHOME

WORKDIR $DockerHOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY . $DockerHOME
RUN pip install -r requirements.txt

EXPOSE 8000

CMD python3 dmcb/manage.py runserver 0.0.0.0:8000
LABEL org.opencontainers.image.source="https://github.com/PapaSinku/dmcb"