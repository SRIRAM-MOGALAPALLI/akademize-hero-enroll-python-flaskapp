# Akademize Hero Enroll Python Flask App

This application provides APIs to make CRUD operations for
Hero Enroll Service.

This application was created in series of step by step development

1. [Crude way of creating APIs, write the data to JSON file](https://github.com/sravanrekandar/akademize-hero-enroll-python-flaskapp/tree/chapter01-json-store)
2. [Using DAO (Data Access Objects)
  and Restful (GET, POST, PUT and DELETE) apis.](https://github.com/sravanrekandar/akademize-hero-enroll-python-flaskapp/blob/chapter02-flaskrestx-approach/src/app.py)

    [Reference from Flask RestX](https://flask-restx.readthedocs.io/en/latest/example.html)

3. **Current implementation**. Using [Sqllite DB](https://www.sqlite.org/index.html) and [SQLAlchemy](https://www.sqlalchemy.org)

## Prerequisites

- Python >= 3.7
- [VSCode IDE](https://code.visualstudio.com/)
  - [VS CODE extension Rest Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)

## Env Setup

```bash
./setup.sh
```

## Start the application

```bash
$ ./start.sh
 * Serving Flask app "app"
 * Forcing debug mode on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 914-428-710
```

## APIs

Open ```requests.http``` in VSCode
