FROM tiangolo/uwsgi-nginx-flask:python3.7
LABEL maintainer="mohamed.keita@nkeita-services.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 80

ENV APP_SETTINGS settings.cfg
ENV FLASK_ENV development
ENV FLASK_DEBUG 1

