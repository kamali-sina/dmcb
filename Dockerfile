# base image  
FROM m.docker-registry.ir/python:3.8-slim-buster
ENV DockerHOME=/home/app/webapp
RUN mkdir -p $DockerHOME

WORKDIR $DockerHOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY . $DockerHOME
RUN pip install -r requirements.txt

EXPOSE 8000

CMD python dmcb/manage.py runserver
