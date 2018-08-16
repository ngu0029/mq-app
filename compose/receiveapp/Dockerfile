# Using official python runtime base image
FROM python:3

# Set the application directory
WORKDIR /app

# Install our requirements.txt
ADD requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy wait-for-it.sh to /app inside the container
ADD wait-for-it.sh /app/wait-for-it.sh

# Copy our code from the current folder to /app inside the container
ADD . /app

# Make ports 5672 5000 8080 available for links and/or publish
EXPOSE 5672 5000 8080

# Define our command to be run when launching the containe
# https://docs.docker.com/compose/startup-order/
CMD ["./wait-for-it.sh", "my-rabbitmq:5672", "--", "python", "recvwebapp.py"]