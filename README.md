# Hydraulic Force Lab

A single-file, **offline** web app that students use during **Day 1** of the TETC
(ExxonMobil Foundation · Teen Engineering + Tech Center) **Hydraulic Rescue Arm** unit.
It makes the force / distance + area-ratio physics something teens can play with, predict
with, and measure their real lab data against.

It is the student-facing companion to the Hydraulic Arm Teacher Guide, and serves the
**Engage** arc of Day 1: _play with it → predict → go measure the real syringes → compare → see the gap._

> The one idea the whole app serves:
> **Force and distance are a single budget. The area ratio (the square of the diameter
> ratio) decides how the budget is spent. The ideal equation always loses a little to
> friction, seal drag, and air. Engineering lives in that gap.**

## Use it

Open `index.html` in a browser. That is the whole app. No install, no accounts, no
network. It works from `file://` or any static server, online or off, including a
school Chromebook with no internet.

### Three tabs

1. **Explore** — pick an input and output syringe diameter (kit presets or free entry).
   See the force multiplier `(d_out / d_in)²` and its inverse distance multiplier live.
   Area circles with unit-square grids make the "squared" relationship countable. Drag
   the plunger to feel force trade for distance on a measured ruler, and a "reality strip"
   previews the friction gap.
2. **Measure** — set your real syringe pair, read the prediction, enter what you measured
   at the bench (forces or distances), and see the gap as two bars. Save each comparison
   to a lab log for your notebook.
3. **Practice** — ten auto-checked challenges that build from the math to design choices.
   A wrong answer gets a nudge, not a buzzer; a second miss reveals the answer so no one
   is stuck.

## Privacy

No accounts, no network, no data collection. Anything saved (the lab log) stays on the
device in `localStorage`. Safe for a school setting by design.

localStorage keys: `hfl:log` (lab log rows), `hfl:lastPair` (last syringe pair).

## Develop / preview

The app is a single hand-authored `index.html` (CSS in `<style>`, JS in `<script>`,
fonts and logo inlined). Vanilla JS, no framework, no build step required at runtime.

To preview locally:

```
node serve.js     # serves this folder on http://localhost:5173
```

(`python3 -m http.server 5173` also works on most machines. The bundled `serve.js`
exists because the macOS preview sandbox used during development could not read the
Desktop folder with the system Python.)

## Fonts

Outfit (headings) and DM Sans (body) are embedded directly in `index.html` as woff2
data URIs, so the app is fully offline. To regenerate them (for example after changing
weights), run:

```
python3 embed_fonts.py
```

This downloads the needed weights from Google Fonts, base64-inlines them, and replaces
the font block in `index.html`.

## Files

- `index.html` — the deliverable (self-contained, offline).
- `serve.js` — tiny static server for local preview.
- `embed_fonts.py` — one-time build step that inlines the fonts.
- `STUDENT_APP_BRIEF.md` — the original design brief.
- `progress.md` — build status and notes.
- `assets copy/` — TETC source assets (the monogram is inlined into the app).

## Known follow-ups

- **Verify the kit syringe diameters.** The presets use sensible standard inner diameters
  (10 mL ≈ 15.9 mm, 20 mL ≈ 20.1 mm, 30 mL ≈ 22.5 mm, 60 mL ≈ 26.6 mm). Confirm these
  against the actual kit before classroom use, since they drive every Measure comparison.
- Optional **Reflect** tab (Day 1 notebook prompts) is not built; it was low priority.

## Design system

Matches the teacher guide: teal `#186172`, magenta `#BD2F7F`, orange `#E8943A`,
turquoise `#0DB4AE`, warm paper background. Voice rules: no em-dashes, no bullet points
in student copy, action-led and plain. Talk to a teen, not down to them.
