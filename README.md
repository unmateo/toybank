# Toybank
#### An approach on modelling a finantial institution API.
----

This project was written on _Python 3.10.3_ and was only tested for that version.
There's a bunch of useful commands available through Makefile.
To avoid dependency conflicts, it's highly recommended to activate a virtual environment before using them.

To start the API for the first time just:
- activate your python3.10 virtualenv
- run `make install-prd && make run`

This will start a server at localhost:8000 and the full API spec will be available at `/openapi.json`.

__PRO tip__: you can explore the API at `/docs`

----

## Developing

The app is built upon [FastAPI](https://fastapi.tiangolo.com/) and [SQLModel](https://sqlmodel.tiangolo.com/).

The code is formatted using [black](https://black.readthedocs.io/) with default parameters.
There's a precommit hook that runs the linter and you can manually run it using `make lint`.

For testing, use [pytest](https://docs.pytest.org/en/7.1.x/), you can run them using `make test`.

## Technical Considerations

The following features have not been developed because of time constraints.
Next to each of them, you'll find how I'd have probably approached them

- logging: a thin layer upon python's standard logging module providing an abstraction over it
- config: [pydantic's settings management](https://pydantic-docs.helpmanual.io/usage/settings/) allows secrets, defaults and validations
- error handling: custom business exceptions that get automatically translated into the suitable API response
  - these should be raised at service layer and handled at router/api layer
- postgresql: most suitable for a production environment
- docker: for easier collaboration, deployment, scaling and monitoring
- docker-compose: for a better development flow

Some notes on the directory structure:

- core: shared components such as the main API, config, logging, database
- models: data models and their API representations
- routers: each component's HTTP rest API capabilities, focusing on input & output
- services: the actual business logic (in this case, mostly persistance)
  - a non HTTP rest API would directly use this layer skipping the routers

## Business considerations:

- unique fields: Customer.email, Account.alias should probably have Unique constraints
- balance: should we enforce a minimum?
- security: should we secure the endpoints? how?
- more generic endpoints as /accounts, /transfers, etc. might me useful
