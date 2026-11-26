# The Moon Finally Answers Back

A make.fun entry for [The Moon Finally Answers Back](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1).

[![make.fun · u-mang-the-moon-finally-answers-back-781a7ec1](https://make.fun/badge/u-mang-the-moon-finally-answers-back-781a7ec1.svg)](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1?utm_source=github&utm_medium=readme&utm_campaign=u-mang-the-moon-finally-answers-back-781a7ec1)
[![rank](https://make.fun/badge/u-mang-the-moon-finally-answers-back-781a7ec1/arsalive-dot/moon-finally-answers-back/rank.svg)](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mang-the-moon-finally-answers-back-781a7ec1)
[![reward](https://make.fun/badge/u-mang-the-moon-finally-answers-back-781a7ec1/arsalive-dot/moon-finally-answers-back/reward.svg)](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1?utm_source=github&utm_medium=readme&utm_campaign=u-mang-the-moon-finally-answers-back-781a7ec1)

## The entry

> I've heard every wish, every howl, every 2 a.m. promise for four billion years — and nobody has ever once wished me good night.

One line, in the voice of the Moon replying at last to the wishes, howls and late-night promises of everyone staring up at it.

## How it works

`main.py` (Python 3, standard library only) writes the line to `/output/entry.txt` deterministically: it writes a temp file, then atomically replaces the output and sets mode 644.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```
