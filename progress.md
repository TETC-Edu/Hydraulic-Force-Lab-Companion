# Hydraulic Force Lab — Progress

_Last updated: 2026-06-03_

Student-facing companion web app for Day 1 of the TETC Hydraulic Rescue Arm unit.
Single-file, offline, vanilla JS + inline SVG. Spec lives in [STUDENT_APP_BRIEF.md](STUDENT_APP_BRIEF.md).

## Status at a glance

**Shipped as v1.0.0 and live.** Fully offline single file, all three tabs done and
verified in the browser. Deployed to GitHub Pages.

- Live: https://tetc-edu.github.io/Hydraulic-Force-Lab-Companion/
- Repo: https://github.com/TETC-Edu/Hydraulic-Force-Lab-Companion (branch `main`, tag `v1.0.0`)

| Tab | State | Notes |
| --- | --- | --- |
| Explore | ✅ Done | Pickers, multipliers, area circles, drag/push sim (diameter-true barrels), rulers, reality strip |
| Measure | ✅ Done | Predict → record → gap bars → localStorage lab log |
| Practice | ✅ Done | 5 auto-checked challenges, nudge-then-reveal feedback |
| Reflect | ⬜ Not built | Optional 4th tab in the brief (low priority) |

## Files

- `index.html` — the deliverable (self-contained, offline: CSS/JS/fonts/logo all inlined). ~481 KB.
- `STUDENT_APP_BRIEF.md` — the original spec / handoff brief.
- `README.md` — real project readme.
- `serve.js` — tiny Node static server for the preview (see Running below).
- `embed_fonts.py` — one-time build: downloads + base64-inlines Outfit/DM Sans woff2 into index.html.
- `set_favicon.py` — one-time build: rebuilds the favicon (monogram arrows) as a base64 SVG data URI.
- `.claude/launch.json` — preview config, name `static`, runs `serve.js` via node.
- `assets copy/` — TETC source assets (monogram SVGs, colors_and_type.css). The monogram is inlined; the rest is reference.
- `progress.md` — this file.

## What's built (detail)

### Explore
- Input/output diameter pickers: kit preset chips (10/20/30/60 mL) + slider + number entry, all synced. Bad input clamps gracefully.
- Live force multiplier `(d_out/d_in)²` and distance multiplier (inverse), plus an adaptive plain-language line.
- **Area circles** with same-size, aligned unit-square grids clipped to each circle (so "squared" is countable), area labels, and an "area ratio = force multiplier" tie-in.
- **Drag/push animation**: input plunger pushes fluid → output lifts a load vertically. Barrels are drawn at the **true diameter ratio** (larger diameter capped to a fixed px size, the other scaled by the same factor) with `Ø … mm` labels, so a fat output that barely rises vs a skinny input that travels far reads as physical. Distance **rulers** on both axes (shared 24px = 1 unit scale) with live "units moved" readouts (value rides to the right of the ruler line; tick numbers on the left). Draggable handle + keyboard (arrows/Home/End) + Push/Reset.
- **Reality strip**: rehearses the Measure gap visual inside the sim — ideal vs typical real (×0.8) force, clearly labeled "typical."
- Three config callouts (1:1, small→big, big→small) that set the pair.

### Measure
- Pair picker (presets + number), prefilled from last Explore pair via `hfl:lastPair`.
- Forces/Distances toggle → computes measured multiplier.
- **Gap visual** matching the teacher guide: teal predicted bar, magenta measured bar, orange gap segment; callout naming % lost + cause chips.
- **Lab log** saved to localStorage (`hfl:log`), persists across reloads, per-row delete + clear all. Note field is full-width.

### Practice
- **5 challenges**, one per concept pillar, escalating: compute the multiplier (12→36 = 9×) → why it is squared (double → quadruple) → force/distance trade (6×, push 30 cm → 5 cm) → design choice (far-and-fast → big→small) → the friction gap (why measured < predicted).
- Numbers are deliberately distinct across questions (mixed ratios 3/2/6, no shared or inverted values) so students must reason, not pattern-match.
- Mixed numeric and multiple-choice. Constructivist feedback: 1st miss → nudge (retry), 2nd miss → reveal answer + explanation and unlock Next (clean first-try solves count toward score; revealed ones don't).
- Progress dots, first-try score on results card, restart. Counter/dots/results scale from the array length.

## Key decisions / conventions

- **Palette/voice**: follows brief §5 (teal/magenta/orange/turquoise; no em-dashes; no bullets in student copy). Brief §5 tokens are the source of truth, not `assets copy/colors_and_type.css` (that's a different deck).
- **localStorage keys**: `hfl:log`, `hfl:lastPair` (wrapped in try/catch). `hfl:reflect` reserved for the Reflect tab.
- **Animation honesty**: the larger of input/output travel is normalized to a fixed budget so both stay on-screen; within a pair the px-per-unit is identical for both, so the ruler/ratio is truthful. Barrel cross-sections use the true diameter ratio. (A 2D side view can't make fluid rectangles equal-area AND show the squared law, so travel uses the real squared ratio; the squared/area idea is carried by the area-circles section.)
- **Animation lifecycle**: `buildAnim()` rebuilds geometry on diameter change (barrels resize); `updateAnim()` only repositions nodes for push/drag, so focus + keyboard + pointer-capture survive a drag. Changing the pair resets the plunger to rest (`animP = 0` in `exSetDia`).
  - ⚠️ Gotcha that bit us twice: the animation geometry object was renamed `G` → `LAY`; a stray `G.sealX0` in the drag handler silently broke dragging (keyboard still worked, hiding it). **When touching the sim, test actual pointer-drag, not just keyboard.**
- **Practice results are NOT persisted** — `pr` state is in-memory and resets on reload. (Relevant to the dashboard idea below.)

## Running the preview

The project lives under `~/Desktop`, which is TCC-protected on macOS. The preview
sandbox's system `python3` cannot read it. Use the Node server instead:
`preview_start` with config name `static` (runs `serve.js`). Port 5173. Do not switch
to `python -m http.server`.

## Deployment

- GitHub Pages, deploy-from-branch: `main` / `/ (root)`. `.nojekyll` present. `index.html` at root.
- Fonts regenerate with `python3 embed_fonts.py`; favicon with `python3 set_favicon.py` (both rewrite index.html). Commit the result; Pages redeploys on push.

## Known gaps / not done

1. **Verify kit diameters (human task — the one real follow-up).** Presets use assumed values (15.9 / 20.1 / 22.5 / 26.6 mm). The brief flagged "verify kit sizes"; these drive every Measure comparison. Needs confirmation against the real kit.
2. **Reflect tab** not built (optional, low priority).
3. Possible later polish (not requested): print stylesheet for the lab log, projector/large-text toggle, `prefers-reduced-motion`, log export/copy, an Explore→Measure handoff button.

## Under discussion (parked): companion analytics dashboard

User wants a dashboard showing aggregate data from the Practice questions. Important
tension: the brief mandates no accounts / no network / no data collection, and explicitly
lists "class dashboards / teacher analytics" as out of scope. Students are minors.

Agreed guardrails if pursued: **anonymous, aggregate-only, ideally no cloud.**
Architecture options discussed:
- **A. Export/import codes (recommended):** each device emits a short code/QR of anonymous results; a second offline `dashboard.html` aggregates. No network, data stays in the room.
- **B. Local classroom server:** devices POST to teacher's laptop over LAN. Real-time, but bends "no network" and adds setup.
- **C. Cloud backend:** easiest UX, but minors' data + compliance + out of scope. Advised against for v1.

Useful (privacy-safe, class-level) metrics: per-question success rate, reveal rate,
**distractor analysis** on multiple-choice, attempts distribution, first-try score.
Prereq: app must first record anonymous practice outcomes locally (not done yet).

Open questions for the user: transport (A/B/C), real-time vs after-class, aggregate-only
vs per-student (recommend aggregate-only), and whether to include Measure gap data too.
