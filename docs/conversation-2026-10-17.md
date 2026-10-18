# Starting conversation — 2026-10-17

Condensed record of the conversation where Sketchstamp started. Decisions that still hold are kept current in `AGENTS.md`; this file is the history.

## 1. Naming the app

**Question:** How would you name an application for sharing hand-drawn square drawings of places (square, church, monument, café) around the world?

**Suggestions, by angle:**
- Square / town square: **Plaza** (town square and square tile), **Piazza**, **Trg** (Serbian for "square"), **Four Corners**
- Hand-drawing: **Placesketch**, **Inkplace**, **Wandersketch**, **Doodlemap**
- Postcards and stamps: **Stamped**, **Postmark**, **Sketchcard**
- Atlas / collection: **Sketch Atlas**, **Atlas of Squares**

Favorites at that point: Plaza (double meaning), Stamped (square, collectible, "I was here"), Placesketch (clarity).

## 2. Does something similar exist?

Yes, but nothing with the same square, collectible format.
- **Sktchr (iPhone)** — closest. Global map of sketch spots, sketches tied to real places, Urban Sketchers meetups. Aimed at practicing artists (planning, light, paint kit). Few ratings yet.
- **SketchMap (Gumroad)** — $10 Leaflet.js tool to pin sketches on a map. Self-hosted, not a community.
- **SketchMap (iOS)** — doodling on top of a map.
- **Draw Maps: Map Notes** — sketching and notes on a map; a utility.
- **Instagram + Urban Sketchers** — the real incumbent; sharing is scattered across Facebook groups and hashtags.

Where we could stand out: the square format as a constraint, collecting / "passport" mechanics, welcoming casual doodlers and not only serious sketchers.

## 3. Urban Sketchers

- Global community and non-profit for drawing on location where people live and travel. Started in 2007 as a Flickr group by Gabriel Campanario (Seattle Times); non-profit since 2009; hundreds of chapters (one recent source says over 450).
- Manifesto: draw on location, not from photos or memory; share online.
- Design choice this raises: **purist mode** (verify GPS and time at upload, as Sktchr does for events) vs **open mode** (drawings from memory or photos allowed).
- Ideas: chapters as groups with meetup pages; pilot with a local chapter (e.g. in Serbia).
- Don't use their name in our branding.

Open question left: aim at the USk on-location crowd or at everyday doodlers?

## 4. Is "Stamped" taken?

Yes — rejected.
- **Stamped (stamped.com, iOS, 2011)** — by former Googlers Robby Stein and Kevin Palms, backed by Google Ventures; users "stamped" places, books and movies, with a map of recommended places. Too close.
- **Stamped.io** — active Shopify reviews app.
- Crowded "stamp + places" space: StampAnytime, Stamplore, Stamp°D, Hexstamp.

Alternatives offered: Inkstamp, **Sketchstamp**, Drawmark; or back to Plaza, Placesketch, Trg.

## 5. Is "Sketchstamp" taken?

No software project or app found. Only generic uses: craft rubber stamps, Procreate "sketch stamp" brushes, "stamp tool" features in drawing apps (Sketch Studio, SolidWorks).

Still to check by hand: domains (.com / .app / .io), App Store and Google Play, trademarks (EUIPO, USPTO — classes 9 and 42), @sketchstamp on Instagram. Small caution: avoid branding resembling the design tool "Sketch."

**Decision: Sketchstamp.**

## 6. Print template

A4 PNG at 300 DPI with two 13 × 13 cm squares, black 0.5 mm border, centered, to print and sketch on.
- First version: ~12 mm even spacing.
- Revised: **21 mm gap** between squares, 8 mm top and bottom margins. That's close to the limit — two 13 cm squares take 260 of 297 mm, and printers can't print the outer 4–5 mm. More space would need smaller squares (e.g. 12.5 cm).
- Print at 100% / Actual size and check the first print with a ruler.

## 7. GitHub description

Options:
1. **Share hand-drawn square sketches of places around the world: squares, churches, monuments, cafés.** ← chosen
2. A map of hand-drawn places. Sketch a square, stamp the spot, share it with the world.
3. Hand-drawn 13×13 sketches of real places, pinned on a world map and collected like stamps.

## 8. AGENTS.md

Created as project memory: what we're building, naming history, landscape, Urban Sketchers notes, ideas, open decisions, assets, working agreements ("read first every prompt, update as we discover"), and a changelog. `CLAUDE.md` contains `@AGENTS.md` so Claude Code reads the same file.

## Sources

- [Sktchr on the App Store](https://apps.apple.com/app/id6781269196)
- [SketchMap on Gumroad](https://yasuhirookura.gumroad.com/l/ramfam)
- [SketchMap on the App Store](https://apps.apple.com/us/app/id6738701125)
- [Draw Maps: Map Notes](https://apps.apple.com/us/app/-/id1291798166)
- [Urban Sketchers Colombo — about USk](https://sites.google.com/view/uskcolombo/about-usc)
- [Urban Sketchers Issaquah/Sammamish](https://issaquahhighlands.com/?p=38969)
- [Urban Sketchers membership / chapters](https://uskmem.clubexpress.com/content.aspx)
- [Former Googlers launch Stamped (9to5Google)](https://9to5google.com/2011/11/21/former-googlers-launch-stamped-a-new-recommendation-app-for-ios/)
- [Stamped.io on Shopify (Digismoothie)](https://www.digismoothie.com/cs/app/stamped-io-reviews)
- [StampAnytime](https://mwm.ai/apps/stampanytime/6761329586)
- [Stamplore](https://apps.apple.com/be/app/stamplore/id6746344238)
- [Stamp°D](https://apps.apple.com/us/app/-/id6743371853)
- [Hexstamp](https://mwm.ai/apps/hexstamp/6785117061)
