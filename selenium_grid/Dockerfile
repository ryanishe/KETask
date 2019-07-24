# Starting from base image
FROM ubuntu:16.04

RUN  apt-get update \
  && apt-get install -y wget \
  && rm -rf /var/lib/apt/lists/*

# Install Python & pip
RUN apt-get update -y && apt-get install -y \
python3 \
python3-pip \
xvfb
RUN pip3 install --upgrade pip

RUN mkdir /tmp/KETests
WORKDIR /tmp/KETests

# Latests Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
  && apt-get update -qqy \
  && apt-get -qqy install \
    google-chrome-stable \
  && rm /etc/apt/sources.list.d/google-chrome.list \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/KETests/requirements.txt
RUN pip3 install -r requirements.txt

RUN apt-get update