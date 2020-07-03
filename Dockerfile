FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN mkdir /opt/django
WORKDIR /opt/django
COPY requirements.txt /opt/django
RUN pip install -r requirements.txt
COPY . /opt/django
