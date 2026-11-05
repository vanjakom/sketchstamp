# Sketchstamp

Share hand-drawn square sketches of places around the world: squares, churches, monuments, cafés.

## The idea

- Draw a place by hand inside a 13 × 13 cm square.
- Photograph or scan it and upload it, tied to the real place.
- Your sketches become a collection of stamps on a world map, and every place gets a page with everyone's drawings of it.

## Print template

`assets/sketch_squares_A4.png` is an A4 page with two 13 × 13 cm squares to sketch in. Print it at **100% / Actual size**. To change the size or spacing, edit the constants in `tools/make_template.py` and run it again.

`assets/sketch_square_A5.png` is an A5 page with a single 13 × 13 cm square. Print it at **100% / Actual size** on A5 paper.

## Storage

Uploaded sketches live in `storage/<user>/`, one file per sketch, named:

```
storage/<user>/<longitude>@<latitude>@<date>.jpg
```

- `longitude`, `latitude` — WGS84 decimal degrees, `.` as the decimal separator, always exactly 5 decimals (about 1 m). Negative values keep their `-` sign (west / south).
- `date` — the day the sketch was drawn, `YYYYMMDD`.
- The image is the inside of the square only: perspective-corrected, black frame trimmed off.

Example: `storage/vanjakom/19.98582@46.17729@20261031.jpg` — Röszke border crossing, drawn 31 Oct 2026.

Every sketch is also listed in `storage/repository.js` (user, longitude, latitude, date, image path). **When you add a sketch, add its entry there too**, or it won't show on the map.

## Map

`index.html` shows all sketches from `storage/repository.js` as pins on a Leaflet map (OpenStreetMap tiles); clicking a pin opens the sketch in a popup. Open it directly from disk or serve the repo root (e.g. GitHub Pages). `index.html?image=<image path>` zooms to one sketch and opens its popup.

## Timeline

`timeline.html` lists all sketches newest first, 10 per page (`?page=2`, …). Each entry shows the date and user, the coordinates (linking to the sketch on the map), and the image. It reads `storage/repository.js`, so new sketches appear automatically.

## Repository layout

```
AGENTS.md                      project memory and rules for agents (read first)
CLAUDE.md                      points Claude Code at AGENTS.md
README.md                      this file
index.html                     map of all sketches (Leaflet)
timeline.html                  all sketches, newest first, 10 per page
storage/repository.js          list of all sketches, read by index.html
assets/sketch_squares_A4.png   printable sketch template (A4, two squares)
assets/sketch_square_A5.png    printable sketch template (A5, one square)
tools/make_template.py         script that generates the A4 template
docs/conversation-2026-10-17.md  how the project started: naming, research, decisions
storage/<user>/                sketches, named <longitude>@<latitude>@<date>.jpg
```

## Status

Idea stage. Name chosen; platform and tech stack not decided yet. See `AGENTS.md` for open decisions.
