FROM python:3.6-alpine

RUN mkdir -p /opt/app
WORKDIR /opt/app

COPY requirements.txt /opt/app/
RUN pip install -r requirements.txt

COPY *.py /opt/app/

ENTRYPOINT ["python", "/opt/app/biirubot.py"]
