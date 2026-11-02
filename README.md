# Sketchstamp

Share hand-drawn square sketches of places around the world: squares, churches, monuments, cafés.

## The idea

- Draw a place by hand inside a 13 × 13 cm square.
- Photograph or scan it and upload it, tied to the real place.
- Your sketches become a collection of stamps on a world map, and every place gets a page with everyone's drawings of it.

## Print template

`assets/sketch_squares_A4.png` is an A4 page with two 13 × 13 cm squares to sketch in. Print it at **100% / Actual size**. To change the size or spacing, edit the constants in `tools/make_template.py` and run it again.

## Storage

Uploaded sketches live in `storage/<user>/`, one file per sketch, named:

```
storage/<user>/<longitude>@<latitude>@<date>.jpg
```

- `longitude`, `latitude` — WGS84 decimal degrees, `.` as the decimal separator, always exactly 5 decimals (about 1 m). Negative values keep their `-` sign (west / south).
- `date` — the day the sketch was drawn, `YYYYMMDD`.
- The image is the inside of the square only: perspective-corrected, black frame trimmed off.

Example: `storage/vanjakom/19.98582@46.17729@20261031.jpg` — Röszke border crossing, drawn 31 Oct 2026.

## Repository layout

```
AGENTS.md                      project memory and rules for agents (read first)
CLAUDE.md                      points Claude Code at AGENTS.md
README.md                      this file
assets/sketch_squares_A4.png   printable sketch template
tools/make_template.py         script that generates the template
docs/conversation-2026-10-17.md  how the project started: naming, research, decisions
storage/<user>/                sketches, named <longitude>@<latitude>@<date>.jpg
```

## Status

Idea stage. Name chosen; platform and tech stack not decided yet. See `AGENTS.md` for open decisions.
