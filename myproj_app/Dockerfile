FROM python:3.9-slim-buster

RUN adduser myproj

WORKDIR /home/myproj

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY *.py ./

RUN chown -R myproj:myproj ./
USER myproj
