import logging

from anime_episode_parser import logger


def pytest_sessionstart() -> None:
    logger.setLevel(logging.DEBUG)
