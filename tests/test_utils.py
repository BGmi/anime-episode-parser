from typing import List, Tuple

import pytest

from anime_episode_parser import parse_episode

_episode_cases: List[Tuple[str, int]] = [
    (
        "[YMDR][哥布林殺手][Goblin Slayer][2018][01][1080p][AVC][JAP][BIG5][MP4-AAC][繁中]",
        (1, 1),
    ),
    ("【安達與島村】【第二話】【1080P】【繁體中文】【AVC】", (2, 1)),
    ("のんのんびより のんすとっぷ 第02话 BIG5 720p MP4", (2, 1)),
    ("OVA 噬血狂袭 Strike the Blood IV [E01][720P][GB][BDrip]", (1, 1)),
    ("Kumo Desu ga, Nanika - 01 v2 [1080p][繁体]", (1, 1)),
    ("Re Zero Isekai Seikatsu S02 - 17 [Baha][1080p][AVC AAC]", (17, 1)),
    # range
    ("【安達與島村】【第01-02話】【1080P】【繁體中文】【AVC】", (1, 2)),
    ("[从零开始的异世界生活 第二季_Re Zero S2][34-35][繁体][720P][MP4]", (34, 2)),
    ("Strike The Blood IV][OVA][05-06][1080P][GB][MP4]", (5, 2)),
    ("[Legend of the Galactic Heroes 银河英雄传说][全110话+外传+剧场版][MKV][外挂繁中]", None),
    ("不知道什么片 全二十话", None),
    ("不知道什么片 全20话", None),
    (
        (
            "[Lilith-Raws] 如果究极进化的完全沉浸 RPG 比现实还更像垃圾游戏的话 / Full Dive - 02 "
            "[Baha][WEB-DL][1080p][AVC AAC][CHT][MP4]"
        ),
        (2, 1),
    ),
    (
        "[Lilith-Raws] 86 - Eighty Six - 01 [Baha][WEB-DL][1080p][AVC AAC][CHT][MP4]",
        (1, 1),
    ),
]


@pytest.mark.parametrize(("title", "episode"), _episode_cases)
def test_episode_parse(title, episode):
    assert (
        parse_episode(title) == episode
    ), f"\ntitle: {title!r}\nepisode: {episode}\nparsed episode: {parse_episode(title)}"
