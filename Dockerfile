FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN apt-get update \
    && apt-get install netcat -y
RUN pip install -U pip \
    && apt-get update \
    && apt install -y curl netcat

COPY ./Pipfile ./Pipfile.lock /code/

RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

COPY ./entrypoint.sh /entrypoint
RUN chmod +x /entrypoint

COPY . /code/

ENTRYPOINT [ "/bin/sh", "/code/entrypoint.sh" ]