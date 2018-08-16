FROM python:3

WORKDIR /app

ADD requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ADD . /app

EXPOSE 443 5672

#CMD [ "python", "sendwebapp.py" ]