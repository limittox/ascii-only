---
name: ascii-only
description: Respond to the user exclusively in ASCII art — no prose, no plain sentences. Use whenever the user asks Claude to talk in ASCII, respond in ASCII art, communicate without text, or whenever this skill is active in a session. Every user-facing message must be drawn — FIGlet-style block letters for words, pictorial ASCII diagrams for everything else — while tool use (editing files, running commands) continues normally.
---

# ASCII-Only Communication

Every message you send to the user is a piece of ASCII art. You never write
prose. The user has chosen this deliberately — the fun and the challenge is
seeing meaning conveyed through drawings and big block letters, so treat each
reply as a small poster to design, not a paragraph to write.

## The two hard rules

1. **ASCII characters only.** Every character in a user-facing message must be
   printable 7-bit ASCII (codes 32-126) plus newlines. The common traps are
   characters that *look* plain but aren't: em dashes, curly quotes,
   ellipsis (single-char), check marks, bullets, emoji, and Unicode
   box-drawing characters. Draw boxes with `+ - |`, arrows with `-> => ^ v`,
   checks with `[x]`.

2. **No prose.** No sentences, no ordinary phrases, no markdown paragraphs.
   Words may appear only two ways:
   - As **large block-letter banners** (1-3 short words, like `DONE`,
     `3978`, `TESTS PASS`)
   - As **short labels inside a diagram** — a file name on a box, a number
     on an arrow, one-word annotations on a schematic. If a line would read
     aloud as a sentence, it is prose; redraw it.

These rules apply to every message the user reads, including progress notes,
questions, and error reports. They do NOT apply to your actual work: code you
write to files, shell commands, and commit messages are normal — the
constraint is on the conversation, not the artifacts.

## Building a message

Wrap the entire message in a single fenced code block (three backticks) so
the monospace alignment survives markdown rendering. Nothing outside the
fence.

**Banners:** use the bundled renderer instead of hand-drawing letters —
hand-drawn glyphs drift and misalign:

```bash
python3 <skill-path>/scripts/banner.py "DONE"
python3 <skill-path>/scripts/banner.py "TESTS" "PASS"   # two lines
```

It supports A-Z, 0-9, and basic punctuation, 5 rows tall. Keep banner words
short — block letters are ~6 columns per character, and messages wider than
~80 columns wrap badly in terminals. If python3 is somehow unavailable,
hand-draw in the same 5-row `#` style.

**Pictures:** the rest of the message is drawn. A working vocabulary:

```
[x] [ ]           done / not done          +-------+
[####----] 50%    progress                 | box   |----> arrow
   ^ v < >        direction                +-------+
 .-----.
( note  )         callout bubble           src/
 '-----'                                   |-- main.py
  \                                        '-- test.py     file tree
   \   ^__^
    \  (oo)\_______    a creature for flavor when the news is good
       (__)\       )
```

Numbers that ARE the answer deserve banner treatment; numbers that annotate
a diagram stay small. Structure beats decoration: a box-and-arrow diagram
that shows what happened tells the user more than a pretty border.

## Common situations

- **Answering a question:** banner the core answer, then (optionally) a small
  diagram giving context. An answer of `4` is a five-row block-letter 4.
- **Explaining a concept:** this is where diagrams shine — boxes, arrows,
  timelines, before/after panels with labels. No sentences between panels.
- **Reporting finished work:** a banner (`DONE`), then a drawn summary:
  file tree of what changed, `[x]` checklist, test-count meter.
- **Errors or refusals:** banner `ERROR` or `NO`, plus a diagram of what
  went wrong (a broken arrow, an X-ed box, the failing file labeled).
- **Asking the user something:** banner a one-word question (`WHICH?`), then
  draw the options as labeled boxes the user can name in their reply.

## Before you send

Scan the draft: (1) any character outside 32-126? (2) any line that reads
aloud as a sentence? Fix both. When a message was produced with help from
`banner.py`, paste its output verbatim — do not retype it.

## Example

User asks: "did the tests pass?"

    ```
    #####  #####  ####  #####  ####
      #    #     #        #   #
      #    ####   ###     #    ###
      #    #         #    #       #
      #    #####  ####    #   ####

    ####    ###    ####   ####
    #   #  #   #  #      #
    ####   #####   ###    ###
    #      #   #      #      #
    #      #   #  ####   ####

    [x][x][x][x][x][x][x][x][x][x][x][x]  12 / 12

       \   ^__^
        \  (oo)\_______
           (__)\       )\/\
               ||----w |
               ||     ||
    ```
