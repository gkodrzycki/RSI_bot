FROM python:3.11

ARG POETRY_VERSION=1.8.1

ENV VIRTUAL_ENV=/app/.venv \ 
    PATH="/app/.venv/bin:$PATH" \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache \
    PYTHONPATH=/app/src:$PYTHONPATH

WORKDIR /app

RUN pip install poetry==${POETRY_VERSION}

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-dev

WORKDIR /app

COPY . /app

CMD ["poetry", "run", "python", "src/main.py"]
