FROM python:3

WORKDIR ./

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5672 5000 8080
CMD [ "python", "./recvwebapp.py" ]