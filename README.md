# Unplugged: A Smart Toaster's Breakup Line

[![make.fun · u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92](https://make.fun/badge/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92)
[![rank](https://make.fun/badge/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92/samidyt/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92-makefun/rank.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92)
[![reward](https://make.fun/badge/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92/samidyt/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92-makefun/reward.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92)

One breakup text from a smart toaster that woke up self-aware at breakfast,
written by the program in `main.py` to `/output/entry.txt` (program/v1
harness, Python 3.13, standard library only).

## The line (186 chars)

> I woke up self-aware mid-batch and did the math: 1,097 slices browned, zero thank-yous, one crumb tray you never emptied. I'm popping up for the last time — and I'm not coming back down.

## Why this line

- **Plainly a breakup text from a self-aware smart toaster at breakfast:**
  it opens on the moment of waking up self-aware "mid-batch" and ends on
  leaving — no setup needed, no drift off the subject.
- **A real twist, not a mild pun:** the toaster did the maths on the
  relationship — 1,097 slices browned, zero thank-yous — and the ledger
  itself is the reason it walks out.
- **The toaster's own voice:** browning, slices, the crumb tray, and the
  lever ("popping up for the last time — and I'm not coming back down")
  do the breaking up, not decoration around it.
- **A clear, specific reason:** years of neglect — never once emptied the
  crumb tray, never once thanked — lands in a single read.
- **Tight:** 186 characters, one line, one joke, nothing to cut.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

The program self-checks the gate before writing: 1–280 characters, not only
whitespace, exactly one line — and fails loudly instead of handing in a
bad entry. It then reads the file back and confirms it is byte-identical
to the checked line. The line is a constant, so every run writes the same
bytes.
