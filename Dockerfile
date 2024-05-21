FROM python:3.12
WORKDIR /opt/

COPY poetry.lock pyproject.toml ./

RUN apt update

RUN pip install --upgrade pip
RUN pip install --no-cache-dir poetry==1.6.*
RUN poetry config virtualenvs.create false
RUN poetry install -n


