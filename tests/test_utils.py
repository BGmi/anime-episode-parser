from typing import List, Tuple, Optional

import pytest

from anime_episode_parser import parse_episode

_episode_cases: List[Tuple[str, Tuple[Optional[int], Optional[int]]]] = [
    (
        "[YMDR][哥布林殺手][Goblin Slayer][2018][01][1080p][AVC][JAP][BIG5][MP4-AAC][繁中]",
        (1, 1),
    ),
    (
        "【安達與島村】【第二話】【1080P】【繁體中文】【AVC】",
        (2, 1),
    ),
    (
        "のんのんびより のんすとっぷ 第02话 BIG5 720p MP4",
        (2, 1),
    ),
    (
        "OVA 噬血狂袭 Strike the Blood IV [E01][720P][GB][BDrip]",
        (1, 1),
    ),
    (
        "Kumo Desu ga, Nanika - 01 v2 [1080p][繁体]",
        (1, 1),
    ),
    (
        "Re Zero Isekai Seikatsu S02 - 17 [Baha][1080p][AVC AAC]",
        (17, 1),
    ),
    # range
    (
        "【安達與島村】【第01-02話】【1080P】【繁體中文】【AVC】",
        (1, 2),
    ),
    (
        "[从零开始的异世界生活 第二季_Re Zero S2][34-35][繁体][720P][MP4]",
        (34, 2),
    ),
    (
        "Strike The Blood IV][OVA][05-06][1080P][GB][MP4]",
        (5, 2),
    ),
    (
        "[Legend of the Galactic Heroes 银河英雄传说][全110话+外传+剧场版][MKV][外挂繁中]",
        (None, None),
    ),
    (
        "不知道什么片 全二十话",
        (None, None),
    ),
    (
        "不知道什么片 全20话",
        (None, None),
    ),
    (
        "[银色子弹字幕组][名侦探柯南][第1005集 36格的完美犯罪（后篇）][繁日双语MP4][1080P]",
        (1005, 1),
    ),
    (
        "[Lilith-Raws] 如果究极进化的完全沉浸 RPG 比现实还更像垃圾游戏的话 / Full Dive - 02 [Baha][WEB-DL][1080p][AVC AAC][CHT][MP4]",
        (2, 1),
    ),
    (
        "[Lilith-Raws] 86 - Eighty Six - 01 [Baha][WEB-DL][1080p][AVC AAC][CHT][MP4]",
        (1, 1),
    ),
    (
        "【幻樱字幕组】【青梅竹马绝对不会输的恋爱喜剧 Osamake】【01~12】【BIG5_MP4】【1280X720】【合集】",
        (1, 12),
    ),
    (
        "【喵萌奶茶屋】★04月新番★[Vivy -Fluorite Eye’s Song-][01-13END][720p][简体][招募翻译校对]",
        (1, 13),
    ),
    (
        "[DBD-Raws][龙珠Z 30周年纪念版/Dragonball Z 30th Anniversary Collection/ドラゴンボール Z][S3][75-107+特典映像][1080P][BDRip][HEVC-10bit][THD+AC3][MKV]",
        (75, 33),
    ),
    (
        "[银色子弹字幕组][名侦探柯南][第1068集 圆谷光彦的侦探笔记][简日双语MP4][1080P]",
        (1068, 1),
    ),
    (
        "[银色子弹字幕组][名侦探柯南][第1071集 工藤优作的推理秀（前篇）][简日双语MP4][1080P]",
        (1071, 1),
    ),
    (
        "[喵萌Production&LoliHouse] 偶像大师 灰姑娘女孩 U149 / THE IDOLM@STER CINDERELLA GIRLS U149 - 03 [WebRip 1080p HEVC-10bit AAC][简繁日内封字幕]",
        (3, 1),
    ),
    (
        "[喵萌Production&LoliHouse] 偶像大师 灰姑娘女孩 U149 / THE IDOLM@STER CINDERELLA GIRLS U149 - 04v2 [WebRip 1080p HEVC-10bit AAC][简繁日内封字幕]",
        (4, 1),
    ),
    (
        "[星火字幕组][填坑][2017-03-18&2017-3-24][名侦探柯南][853-854][樱花班的回忆][生肉无字幕[1080P][MP4]",
        (853, 2),
    ),
    (
        "乡下大叔成为剑圣 / 乡下大叔成为剑圣 - EP02 [简 / 繁] (1080p AMZN WEB-DL H.264 AAC2.0+DDP2.0 SRTx2)",
        (2, 1),
    ),
    (
        "六四位元字幕组★重启人生的千金小姐正在攻略龙帝陛下 Yarinaoshi Reijou wa Ryuutei Heika o Kouryakuchuu★11★1920x1080★AVC AAC MP4★繁体中文",
        (11, 1),
    ),  
]


@pytest.mark.parametrize(("title", "episode"), _episode_cases)
def test_episode_parse(
    title: str,
    episode: Tuple[Optional[int], Optional[int]],
) -> None:
    assert (
        parse_episode(title) == episode
    ), f"\ntitle: {title!r}\nepisode: {episode}\nparsed episode: {parse_episode(title)}"
