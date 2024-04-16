FROM python:3.10

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install --upgrade pip && pip install poetry
RUN poetry config virtualenvs.create false && poetry install

COPY . .

EXPOSE 5000

ENV FLASK_APP=flask_crud/main.py

CMD [ "poetry", "run", "flask", "run", "--host=0.0.0.0", "--port=5000" ]
