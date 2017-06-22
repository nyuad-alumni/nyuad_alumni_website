FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /src
WORKDIR /src
ADD requirements.txt /src
RUN pip install --no-cache-dir -r requirements.txt
ADD . /src
