FROM mcr.microsoft.com/playwright/python:v1.20.0-focal

ADD requirements.txt /

RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

RUN pip install --upgrade pip && \
    pip install virtualenv && \
    virtualenv --python=/usr/bin/python3 /opt/venv && \
    . /opt/venv/bin/activate && \
    pip install -r requirements.txt --quiet

WORKDIR /app
