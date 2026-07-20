# ascii-only

A [Claude Code](https://claude.com/claude-code) skill that makes Claude
respond to the user exclusively in ASCII art — no prose, no plain sentences.
Words only appear as large block-letter banners or short labels inside
diagrams; everything else is drawn with plain 7-bit ASCII characters.

```
####   ###  #   # #####
#   # #   # ##  # #
#   # #   # # # # ####
#   # #   # #  ## #
####   ###  #   # #####

[x] python3 fizzbuzz.py  ->  exit 0
lines    [##############################] 30 / 30
```

## Install

Copy the skill into your Claude Code skills directory:

```bash
cp -r ascii-only ~/.claude/skills/
```

Once installed, ask Claude to "respond in ASCII only" or "talk to me in
ASCII art" to trigger it, or reference it directly with `/ascii-only`.

## How it works

See [`ascii-only/SKILL.md`](ascii-only/SKILL.md) for the full instructions
Claude follows. In short:

- **ASCII only** — every character must be printable 7-bit ASCII (codes
  32-126) plus newlines. No em dashes, curly quotes, emoji, or Unicode
  box-drawing characters.
- **No prose** — words appear only as block-letter banners (`DONE`, `3978`)
  or short labels inside a diagram (a filename on a box, a number on an
  arrow). Anything that reads aloud as a sentence gets redrawn instead.
- Tool use (editing files, running commands, commit messages) is unaffected
  — the constraint applies only to what Claude sends back to the user.

The skill bundles [`scripts/banner.py`](ascii-only/scripts/banner.py), a
small renderer that turns text into consistent 5-row block letters, so
Claude doesn't hand-draw wobbly glyphs.

## Evals

[`ascii-only/evals/evals.json`](ascii-only/evals/evals.json) has three test
prompts (a quick math question, a coding task with a report-back, and a
concept explanation). `ascii-only-workspace/iteration-1/` holds the results
of running each prompt with and without the skill, graded against
assertions like "response is pure ASCII" and "no prose sentences."

| | With skill | Without skill |
|---|---|---|
| Assertions passed | 100% | 44% |

The baseline failures were non-ASCII characters (em dashes) and ordinary
prose paragraphs — exactly what the skill is designed to prevent.
