FROM python:3.7

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 80

CMD [ "python", "app.py" ]