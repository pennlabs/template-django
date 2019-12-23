# Django Template

This template repo contains all the sample configuration needed to create a fully functioning django app 
following all of Penn Labs's suggested configuration.

## Installation
Make sure django is installed globally: `pip3 install --user django`

- `django-admin startproject --template=https://github.com/pennlabs/template-django/archive/master.zip --extension=py,cfg,yaml --name=Dockerfile <project name>`
- `cd <project name>`
- `pipenv install --dev` to install all packages needed
- After creating apps, make sure to add them to `known_first_party` in `setup.cfg`.
- `mv circleci .circleci` to enable continuous integration and deployment.

## Features

* CircleCI:
  * Workflow to test, build, publish, and deploy your django project using contexts to keep secrets safe
* Django
  * Multiple settings environments (development, production, and ci) each with specific configuration
    * CI
      * Configuration to upload test results to CircleCI
    * Production
      * Disable debug
      * Enable emoji support
      * Enable sentry reporting
      * Restrict `ALLOWED_HOSTS`
  * Configure Penn Labs accounts (in production and development)
  * Renamed admin interface
* Docker
  * .dockerignore file to prevent unnecessary files from being added to the docker image
  * Dockerfile to create a docker image to run your django project
* Git
  * .gitignore file to prevent common unnecessary files from being committed
* MIT License
* Python
  * Common dependencies pre-configured, split into regular and development packages
  * Testing, linting, code coverage, and uwsgi configuration

Also see [django-labs-accounts](https://github.com/pennlabs/django-labs-accounts) for configuration specific to Penn Labs accounts.
