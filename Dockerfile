FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN apt-get update && \
    apt-get install -y locales && \
    sed -i -e 's/# pt_BR.UTF-8 UTF-8/pt_BR.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=nointeractive locales

ENV LC_ALL=pt_BR.UTF-8
ENV LANG=pt_BR.UTF-8

WORKDIR app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/