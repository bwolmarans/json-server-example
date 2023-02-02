FROM python:3.8-slim-buster
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN apt-get -qq update 
RUN apt-get -qq -y install curl
RUN apt-get -qq -y install vim
RUN apt-get -qq -y install net-tools

COPY . .

CMD [ "python3", "widgets-app-frontend.py", "8080"]
