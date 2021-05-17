# anime-episode-parser

try parse episode info from title

```bash
poetry add anime_episode_parser
```

```python3
from anime_episode_parser import parse_episode

title = '[YMDR][哥布林殺手][Goblin Slayer][2018][05][1080p][AVC][JAP][BIG5][MP4-AAC][繁中]'
assert (5, 1) == parse_episode(title)

# 5 for episode start
# 1 for episodes count

title = '[从零开始的异世界生活 第二季_Re Zero S2][34-35][繁体][720P][MP4]'
assert (34, 2) == parse_episode(title)

# 34 for episode start
# 2 for episodes count
```
