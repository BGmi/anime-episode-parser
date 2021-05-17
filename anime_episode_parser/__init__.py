import re
import logging
from typing import List, Tuple, Union

from anime_episode_parser.cn import chinese_to_arabic

logger = logging.getLogger("anime-episode-parser")


FETCH_EPISODE_WITH_BRACKETS = re.compile(r"[【\[]E?(\d+)\s?(?:END)?[】\]]")

FETCH_EPISODE_ZH = re.compile(r"第?\s?(\d{1,3})\s?[話话集]")
FETCH_EPISODE_ALL_ZH = re.compile(r"第([^第]*?)[話话集]")
FETCH_EPISODE_ONLY_NUM = re.compile(r"^([\d]{2,})$")

FETCH_EPISODE_RANGE = re.compile(r"[^sS][\d]{2,}\s?-\s?([\d]{2,})")
FETCH_EPISODE_RANGE_ZH = re.compile(r"[第][\d]{2,}\s?-\s?([\d]{2,})\s?[話话集]")
FETCH_EPISODE_RANGE_ALL_ZH_1 = re.compile(r"[全]([\d-]*?)[話话集]")
FETCH_EPISODE_RANGE_ALL_ZH_2 = re.compile(r"第?(\d-\d)[話话集]")

FETCH_EPISODE_OVA_OAD = re.compile(r"([\d]{2,})\s?\((?:OVA|OAD)\)]")
FETCH_EPISODE_WITH_VERSION = re.compile(r"[【\[](\d+)\s? *v\d(?:END)?[】\]]")

FETCH_EPISODE = (
    FETCH_EPISODE_ZH,
    FETCH_EPISODE_ALL_ZH,
    FETCH_EPISODE_WITH_BRACKETS,
    FETCH_EPISODE_ONLY_NUM,
    FETCH_EPISODE_RANGE,
    FETCH_EPISODE_RANGE_ALL_ZH_1,
    FETCH_EPISODE_RANGE_ALL_ZH_2,
    FETCH_EPISODE_OVA_OAD,
    FETCH_EPISODE_WITH_VERSION,
)


def get_real_episode(episode_list: Union[List[str], List[int]]) -> int:
    return min(int(x) for x in episode_list)


def parse_episode(episode_title: str) -> Union[Tuple[int, int], None]:
    """
    parse episode from title
    :param episode_title: episode title
    :type episode_title: str
    :return: episode of this title
    :rtype: int
    """
    spare = None

    for pattern in (FETCH_EPISODE_RANGE_ALL_ZH_1, FETCH_EPISODE_RANGE_ALL_ZH_2):
        _ = pattern.findall(episode_title)
        if _ and _[0]:
            logger.debug("return episode range all zh '%s'", pattern.pattern)
            return None

    _ = FETCH_EPISODE_RANGE.findall(episode_title)
    if _ and _[0]:
        logger.debug("return episode range")
        return None

    _ = FETCH_EPISODE_RANGE_ZH.findall(episode_title)
    if _ and _[0]:
        logger.debug("return episode range zh")
        return None

    _ = FETCH_EPISODE_ZH.findall(episode_title)
    if _ and _[0].isdigit():
        logger.debug("return episode zh")
        return int(_[0]), 1

    _ = FETCH_EPISODE_ALL_ZH.findall(episode_title)
    if _ and _[0]:
        try:
            logger.debug("try return episode all zh %s", _)
            e = chinese_to_arabic(_[0])
            logger.debug("return episode all zh")
            return e, 1
        except Exception:
            logger.debug("can't convert %s to int", _[0])

    _ = FETCH_EPISODE_WITH_VERSION.findall(episode_title)
    if _ and _[0].isdigit():
        logger.debug("return episode range with version")
        return int(_[0]), 1

    _ = FETCH_EPISODE_WITH_BRACKETS.findall(episode_title)
    if _:
        logger.debug("return episode with brackets")
        return get_real_episode(_), 1

    logger.debug("don't match any regex, try match after split")
    rest: List[int] = []
    for i in episode_title.replace("[", " ").replace("【", ",").split(" "):
        for regexp in FETCH_EPISODE:
            match = regexp.findall(i)
            if match and match[0].isdigit():
                m = int(match[0])
                if m > 1000:
                    spare = m
                else:
                    logger.debug(f"match {i} '{regexp.pattern}' {m}")
                    rest.append(m)

    if rest:
        return get_real_episode(rest), 1

    if spare:
        return spare, 1

    return None
