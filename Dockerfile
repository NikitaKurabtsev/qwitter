FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY Pipfile Pipfile.lock /app/
RUN pip install --upgrade pip && pip install pipenv && pipenv install --system

COPY . /app/