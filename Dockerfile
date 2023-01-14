FROM ubuntu:latest

RUN apt update
RUN apt upgrade
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN pip3 install flask
RUN mkdir /app