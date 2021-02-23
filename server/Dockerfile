FROM python:3.10.0a5-alpine3.13

#pour print les connexions dans le terminal
ENV PYTHONUNBUFFERED=1 
WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt

RUN apk add npm
RUN npm install bower
RUN apk add git
RUN echo '{ "allow_root": true }' > /root/.bowerrc
RUN /code/node_modules/bower/bin/bower install material-cards
RUN mv bower_components ./app/static/lib/



