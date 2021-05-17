import sys
import logging

from anime_episode_parser import logger


def sessionstart(*args, **kwargs):
    logger.addHandler(logging.StreamHandler(sys.stdout))
