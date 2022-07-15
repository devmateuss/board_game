FROM python:latest

WORKDIR /usr/app/src

ADD ./ ./

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

CMD [ "python", "./main.py"]