FROM python:3.10.0a5-alpine3.13


ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt

# Download npm
#FROM debian
#RUN apt-get update
# -y pour forcer le telechargement
#RUN apt-get -y install npm
#RUN apt-get install -y  git

#RUN npm install -g bower 
#on Autorise l'accès au telechargement avec bower
#RUN echo '{ "allow_root": true }' > /root/.bowerrc
#RUN bower install material-cards
