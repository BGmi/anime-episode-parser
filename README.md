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
# `None` for un-determined episode
# episode range is not implemented yet.
```
