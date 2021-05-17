import logging

from anime_episode_parser import logger


def pytest_sessionstart():
    logger.setLevel(logging.DEBUG)
