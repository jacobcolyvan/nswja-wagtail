ARG PYTHON_VERSION=3.13-slim
ARG NODE_VERSION=24-slim

FROM node:${NODE_VERSION} AS frontend

WORKDIR /code

# Copy pnpm package files
COPY package.json pnpm-lock.yaml /code/

# Install pnpm
ARG PNPM_VERSION=11.17.0
RUN npm install -g pnpm@${PNPM_VERSION}

# Install dependencies using pnpm
RUN pnpm install --frozen-lockfile

# Copy static files for CSS build
COPY static /code/static
COPY templates /code/templates

# Build Tailwind CSS
COPY tailwind.config.js /code/
RUN pnpm run css:build

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install django/wagtail/psycopg dependencies.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    libmariadb-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
    gcc \
  && rm -rf /var/lib/apt/lists/*


RUN mkdir -p /code

WORKDIR /code

RUN pip install uv

# Install the project requirements using uv
COPY pyproject.toml /code/
RUN uv pip install -r /code/pyproject.toml --system

EXPOSE 8000

COPY . /code/
COPY --from=frontend /code/static/css/output.css /code/static/css/output.css

# Collect static files.
RUN python manage.py collectstatic --noinput --clear

CMD ["gunicorn", \
    "--bind", ":8000", \
    "--workers", "4", \
    "--timeout", "60", \
    "--max-requests", "1000", \
    "--max-requests-jitter", "100", \
    "djangosite.wsgi"]
