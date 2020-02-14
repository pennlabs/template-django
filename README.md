# Django Template

This template repo contains all the sample configuration needed to create a fully functioning django app following all of Penn Labs's suggested configuration.

## Installation

Click the green "Use this template" button and make a new repo with your desired name. Run the provided init script `./init.sh <name of project> <name of github repo>` to configure most of the project. See the configuration section for final changes that need to be made.

## Features

- CircleCI:
  - Workflow to test, build, publish, and deploy your django project using contexts to keep secrets safe
- Django
  - Multiple settings environments (development, production, and ci) each with specific configuration
    - CI
      - Configuration to upload test results to CircleCI
    - Production
      - Disable debug
      - Enable emoji support
      - Enable sentry reporting
      - Restrict `ALLOWED_HOSTS`
  - Configure Penn Labs accounts (in production and development)
  - Renamed admin interface
- Docker
  - .dockerignore file to prevent unnecessary files from being added to the docker image
  - Dockerfile to create a docker image to run your django project
- Git
  - .gitignore file to prevent common unnecessary files from being committed
- MIT License
- Python
  - Common dependencies pre-configured, split into regular and development packages
  - Testing, linting, code coverage, and uwsgi configuration

## Configuration

Edit the values in `k8s/values.yml` to reflect the domain of the django project as well as any secrets it needs.
Additionally provide a description of the project in `README.md`

Also see [django-labs-accounts](https://github.com/pennlabs/django-labs-accounts) for configuration specific to Penn Labs accounts.
