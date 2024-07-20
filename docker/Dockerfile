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
    PYSETUP_PATH="/roominar" \
    VENV_PATH="/roominar/.venv"

# prepend poetry and venv to path
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# `builder-base` stage is used to build deps + create our virtual environment
FROM python-base as builder-base
RUN apt-get update && apt-get install --no-install-recommends -y \
    # deps for installing poetry
    curl \
    # deps for building python deps
    libpq-dev build-essential


# Install poetry - respects $POETRY_VERSION & $POETRY_HOME
RUN curl -sSL https://install.python-poetry.org | python

# Copy project requirement files here to ensure they will be cached.
# We will cache our requirements and only reinstall them when pyproject.toml or poetry.lock files change. Otherwise builds will be slow.
WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./
COPY ./app /roominar/app/

# Install runtime deps - uses $POETRY_VIRTUALENVS_IN_PROJECT internally
RUN poetry install --only main

# `development` image is used during development / testing
FROM python-base as development
ENV FASTAPI_ENV=development

# Copy in our built poetry + venv
COPY --from=builder-base $POETRY_HOME $POETRY_HOME
COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH

RUN apt-get update && apt-get install --no-install-recommends -y \
    libpq-dev build-essential git bash curl tar sudo default-jre && \
    useradd -m -d /home/roominar -s /bin/bash roominar && \
    chown roominar /home/roominar && \
    echo 'roominar ALL=(ALL) NOPASSWD:ALL' >>/etc/sudoers && \
    curl -sS https://starship.rs/install.sh | sh -s -- --yes && \
    echo 'eval "$(starship init bash)"' >>/home/roominar/.bashrc && \
    rm -rf /var/lib/apt/lists/*

USER roominar
WORKDIR $PYSETUP_PATH

RUN poetry install

WORKDIR /roominar

EXPOSE 8000
CMD ["uvicorn", "--reload", "app.main:app"]
