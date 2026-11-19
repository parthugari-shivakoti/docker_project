# FastAPI Docker CI

![CI](https://github.com/parthugari-shivakoti/docker_project/actions/workflows/ci.yml/badge.svg)

A FastAPI project demonstrating:

- REST API development using FastAPI
- Automated testing with Pytest
- Code linting using Ruff
- Docker containerization
- GitHub Actions CI

## Run Locally

Install dependencies:

    pip install -r requirements.txt

Start the server:

    uvicorn main:app --reload

## Run Tests

    python -m pytest -v

## Lint

    ruff check .

## Build Docker Image

    docker build -t fastapi-ci-app:latest .
