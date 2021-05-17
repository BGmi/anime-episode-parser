# Contributing

## setup your dev env

project is managed by [`poetry`](https://github.com/python-poetry/poetry)

```bash
poetry install
```

## lint

```bash
pre-commit run --all-files
mypy anime_episode_parser
flake8 anime_episode_parser
```

## test

```bash
pytest
```
