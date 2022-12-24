FROM python:3.8.10-alpine

RUN mkdir /app

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
ADD requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/

CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "collectstatic"]
CMD ["python", "manage.py", "runserver" ,"0.0.0.0:8081", "--noreload"]
