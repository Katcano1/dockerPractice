FROM python:3.12
WORKDIR /opt/

COPY poetry.lock pyproject.toml ./

RUN apt-get update

RUN pip install --upgrade pip
RUN pip install --no-cache-dir poetry==1.8.*
RUN poetry config virtualenvs.create false
RUN poetry install -n

CMD ["python", "/QuickStart+.py"]


