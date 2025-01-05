ARG PYTHON_VERSION=3.13-slim

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
    nodejs \
    npm \
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

# Install pnpm
RUN npm install -g pnpm

# Copy package files
COPY package.json pnpm-lock.yaml* /code/

# Install dependencies using pnpm
RUN pnpm install

# Build Tailwind CSS using pnpm
RUN pnpm run css:build

# Collect static files.
RUN python manage.py collectstatic --noinput --clear

CMD ["gunicorn","--bind",":8000","--workers","1","djangosite.wsgi"]
