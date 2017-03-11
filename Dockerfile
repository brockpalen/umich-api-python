FROM python:3

MAINTAINER brockp@umich.edu

ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

ADD . /code
WORKDIR /code

CMD ["python", "oauthtest.py"]
