import re
import logging
from typing import List, Tuple, Union, Callable, Optional

from anime_episode_parser.cn import chinese_to_arabic

logger = logging.getLogger("anime-episode-parser")


_EPISODE_WITH_BRACKETS = re.compile(r"[【\[]E?(\d+)\s?(?:END)?[】\]]")

_EPISODE_ZH = re.compile(r"第?\s?(\d{1,4})\s?[話话集]")
_EPISODE_ALL_ZH = re.compile(r"第([^第]*?)[話话集]")
_EPISODE_ONLY_NUM = re.compile(r"^([\d]{2,})$")

_EPISODE_RANGE = re.compile(r"[^sS]([\d]{2,})\s?[-~]\s?([\d]{2,})")
_EPISODE_RANGE_ZH = re.compile(r"[第]([\d]{2,})\s?[-~]\s?([\d]{2,})\s?[話话集]")
_EPISODE_RANGE_ALL_ZH_1 = re.compile(r"[全]([\d-]*?)[話话集]")
_EPISODE_RANGE_ALL_ZH_2 = re.compile(r"第?(\d*)\s?[-~]\s(\d*)[話话集]")

_EPISODE_OVA_OAD = re.compile(r"([\d]{2,})\s?\((?:OVA|OAD)\)]")
_EPISODE_WITH_VERSION = re.compile(r"[【\[](\d+)\s? *v\d(?:END)?[】\]]")

_PATTERNS = (
    _EPISODE_ZH,
    _EPISODE_ALL_ZH,
    _EPISODE_WITH_BRACKETS,
    _EPISODE_ONLY_NUM,
    _EPISODE_RANGE,
    _EPISODE_RANGE_ALL_ZH_1,
    _EPISODE_RANGE_ALL_ZH_2,
    _EPISODE_OVA_OAD,
    _EPISODE_WITH_VERSION,
)


def get_real_episode(episode_list: Union[List[str], List[int]]) -> int:
    return min(int(x) for x in episode_list)


def episode_range(
    e: Tuple[str, str],
    convert: Callable[[str], int] = int,
) -> Tuple[int, int]:
    _ = e[0]
    _0 = convert(_[0])
    _1 = convert(_[1])
    return _0, _1 - _0 + 1


def parse_episode(episode_title: str) -> Tuple[Optional[int], Optional[int]]:
    """
    parse episode from title
    :param episode_title: episode title
    :type episode_title: str
    :return: episode of start, episode count
    """
    spare = None

    _ = _EPISODE_RANGE_ALL_ZH_1.findall(episode_title)
    if _ and _[0]:
        logger.debug("matching with _EPISODE_RANGE_ALL_ZH_1 '%s'", _)
        return None, None

    _ = _EPISODE_RANGE_ALL_ZH_2.findall(episode_title)
    if _ and _[0]:
        logger.debug("matching with EPISODE_RANGE_ALL_ZH_2 %s", _)
        return episode_range(_)

    _ = _EPISODE_RANGE.findall(episode_title)
    if _ and _[0]:
        logger.debug("matching with EPISODE_RANG %s", _)
        return episode_range(_)

    _ = _EPISODE_RANGE_ZH.findall(episode_title)
    if _ and _[0]:
        logger.debug("return episode range zh")
        return int(_[0]), int(_[1]) - int(_[0])

    _ = _EPISODE_ZH.findall(episode_title)
    if _ and _[0].isdigit():
        logger.debug("return episode zh")
        return int(_[0]), 1

    _ = _EPISODE_ALL_ZH.findall(episode_title)
    if _ and _[0]:
        try:
            logger.debug("try return episode all zh %s", _)
            e = chinese_to_arabic(_[0])
            logger.debug("return episode all zh")
            return e, 1
        except Exception:
            logger.debug("can't convert %s to int", _[0])

    _ = _EPISODE_WITH_VERSION.findall(episode_title)
    if _ and _[0].isdigit():
        logger.debug("return episode range with version")
        return int(_[0]), 1

    _ = _EPISODE_WITH_BRACKETS.findall(episode_title)
    if _:
        logger.debug("return episode with brackets")
        return get_real_episode(_), 1

    logger.debug("don't match any regex, try match after split")
    rest: List[int] = []
    for i in episode_title.replace("[", " ").replace("【", ",").split(" "):
        for regexp in _PATTERNS:
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

    return None, None
