FROM python:3.9.9
WORKDIR /usr/src/
COPY requirements.txt ./

RUN apt update
RUN apt install libgl1-mesa-glx -y
RUN pip install -r requirements.txt

ENV PYTHONPATH="/usr/src/"

COPY . /usr/src/
