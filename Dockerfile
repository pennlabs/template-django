FROM pennlabs/django-base

MAINTAINER Penn Labs

# Copy project dependencies
ONBUILD COPY Pipfile* /app/

# Install project dependencies
ONBUILD RUN pipenv install --system

# Copy project files
ONBUILD COPY . /app/

# Collect static files
ONBUILD RUN python3.7 /app/manage.py collectstatic --noinput
