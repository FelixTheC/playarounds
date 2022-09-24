FROM python:3.10.7-buster

RUN sudo apt update

RUN curl -sSL https://install.python-poetry.org | python3 -

# Configure Poetry
ENV POETRY_VERSION=1.2.0
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv
ENV POETRY_CACHE_DIR=/opt/.cache

RUN mkdir app

COPY ./eisenhower_matrix /app

WORKDIR app
RUN poetry install