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

For testing, we use [pytest](https://docs.pytest.org/en/7.1.x/), you can run them using `make test`.
