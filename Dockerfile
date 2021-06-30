FROM python

WORKDIR /app

RUN pip install flask
RUN pip install pyyaml
RUN pip install flask-mysqldb

COPY . .

EXPOSE 81

CMD python app.py