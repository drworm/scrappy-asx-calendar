FROM python:3.6

WORKDIR /cwd
ADD ./requirements.txt .

RUN pip install -r requirements.txt
ADD . /cwd
