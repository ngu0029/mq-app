FROM python:3

WORKDIR /app

ADD requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ADD . /app

EXPOSE 5000

#CMD [ "python", "httpserver.py" ]