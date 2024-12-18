FROM python:3

RUN pip install flask-mysqldb
RUN pip install mysql-connector-python

RUN mkdir -p /srv/templates
COPY index.html /srv/templates/index.html
COPY app_1.py /srv/app1.py

CMD ["flask","--app","/srv/app1","run","--host=0.0.0.0"]

