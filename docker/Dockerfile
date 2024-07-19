FROM python:3.11.5-slim as python-base

# python
ENV PYTHONUNBUFFERED=1 \
    # prevents python creating .pyc files
    PYTHONDONTWRITEBYTECODE=1 \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # poetry
    # https://python-poetry.org/docs/configuration/#using-environment-variables
    POETRY_VERSION=1.6.1 \
    # make poetry install to this location
    POETRY_HOME="/opt/poetry" \
    # make poetry create the virtual environment in the project's root
    # it gets named `.venv`
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    # do not ask any interactive question
    POETRY_NO_INTERACTION=1 \
    # paths
    # this is where our requirements + virtual environment will live
    PYSETUP_PATH="/workspace" \
    VENV_PATH="/workspace/.venv"

# prepend poetry and venv to path
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

FROM python-base as poetry-base
RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    # deps for installing poetry
    curl

# install poetry - respects $POETRY_VERSION & $POETRY_HOME
# Official way to install Poetry
RUN curl -sSL https://install.python-poetry.org | python

# `builder-base` stage is used to build deps + create our virtual environment
FROM poetry-base as builder-base
RUN apt-get update && \
    apt-get install --no-install-recommends -y  \
    # deps for building python deps
    build-essential \
    libpq-dev

# Copy project requirement files here to ensure they will be cached.
# We will cache our requirements and only reinstall them when pyproject.toml or poetry.lock files change. Otherwise builds will be slow.
WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./
COPY ./app /workspace/app/

# install runtime deps - uses $POETRY_VIRTUALENVS_IN_PROJECT internally
RUN poetry install --only main

# `development` image is used during development / testing
FROM python-base as development

RUN useradd --create-home -d /home/app --shell /bin/bash app

# copy in our built poetry + venv
COPY --from=poetry-base $POETRY_HOME $POETRY_HOME

RUN apt-get update && apt-get install --no-install-recommends -y \
    libpq-dev build-essential git bash curl tar sudo default-jre && \
    echo '%app ALL=(ALL) NOPASSWD:ALL' >>/etc/sudoers && \
    curl -sS https://starship.rs/install.sh | sh -s -- --yes && \
    echo 'eval "$(starship init bash)"' >>/home/app/.bashrc && \
    rm -rf /var/lib/apt/lists/*

COPY . .

USER app

# will become mountpoint of our code
WORKDIR /workspace


EXPOSE 8000
CMD ["poetry", "run", "uvicorn", "--reload", "app.main:app"]


# `production` image used for runtime
# FROM python-base as production
# ENV FASTAPI_ENV=production
# COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH
# COPY ./app /app/
# WORKDIR /app
# CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "main:app"]
