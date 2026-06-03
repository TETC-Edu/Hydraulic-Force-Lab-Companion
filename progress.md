# Hydraulic Force Lab — Progress

_Last updated: 2026-06-02_

Student-facing companion web app for Day 1 of the TETC Hydraulic Rescue Arm unit.
Single-file, offline, vanilla JS + inline SVG. Spec lives in [STUDENT_APP_BRIEF.md](STUDENT_APP_BRIEF.md).

## Status at a glance

All four MVP milestones are built and verified in the browser preview. The app is
feature-complete for Day 1 Engage, but is **not yet truly offline** (see Known gaps).

| Tab | State | Notes |
| --- | --- | --- |
| Explore | ✅ Done | Pickers, multipliers, area circles, drag/push animation, rulers, reality strip |
| Measure | ✅ Done | Predict → record → gap bars → localStorage lab log |
| Practice | ✅ Done | 10 auto-checked challenges, nudge-then-reveal feedback |
| Reflect | ⬜ Not built | Optional 4th tab in the brief (low priority) |

## Files

- `index.html` — the deliverable (self-contained app: CSS in `<style>`, JS in `<script>`).
- `STUDENT_APP_BRIEF.md` — the original spec / handoff brief.
- `serve.js` — tiny Node static server for the preview (see Running below).
- `.claude/launch.json` — preview config, name `static`, runs `serve.js` via node.
- `assets copy/` — TETC source assets (monogram SVGs, colors_and_type.css). The monogram
  is inlined into the top bar; the rest is reference.
- `progress.md` — this file.

## What's built (detail)

### Explore
- Input/output diameter pickers: kit preset chips (10/20/30/60 mL) + slider + number entry, all synced. Bad input clamps gracefully.
- Live force multiplier `(d_out/d_in)²` and distance multiplier (inverse), plus an adaptive plain-language line.
- **Area circles** with same-size, aligned unit-square grids clipped to each circle (so "squared" is countable), area labels, and an "area ratio = force multiplier" tie-in.
- **Drag/push animation**: input plunger pushes fluid → output lifts a load vertically. Built once, repositioned per frame (focus/keyboard/pointer-capture all survive a drag). Distance **rulers** on both axes (shared scale) with live "units moved" readouts.
- **Reality strip**: rehearses the Measure gap visual inside the sim — ideal vs typical real (×0.8) force, clearly labeled "typical."
- Three config callouts (1:1, small→big, big→small) that set the pair.

### Measure
- Pair picker (presets + number), prefilled from last Explore pair via `hfl:lastPair`.
- Forces/Distances toggle → computes measured multiplier.
- **Gap visual** matching the teacher guide: teal predicted bar, magenta measured bar, orange gap segment; callout naming % lost + cause chips.
- **Lab log** saved to localStorage (`hfl:log`), persists across reloads, per-row delete + clear all. Note field is full-width.

### Practice
- 10 challenges escalating: calculate → reason about the square → design choices → the friction gap (bridges to Measure).
- Mixed numeric and multiple-choice. Constructivist feedback: 1st miss → nudge (retry), 2nd miss → reveal answer + explanation and unlock Next (clean first-try solves count toward score; revealed ones don't).
- Progress dots, first-try score on results card, restart.

## Key decisions / conventions

- **Palette/voice**: follows brief §5 (teal/magenta/orange/turquoise; no em-dashes; no bullets in student copy). Brief §5 tokens are the source of truth, not `assets copy/colors_and_type.css` (that's a different deck).
- **localStorage keys**: `hfl:log`, `hfl:lastPair` (wrapped in try/catch). `hfl:reflect` reserved for the Reflect tab.
- **Animation honesty**: the larger of input/output travel is normalized to a fixed budget so both stay on-screen; within a pair the px-per-unit is identical for both, so the ruler/ratio is truthful.
- **Practice results are NOT persisted** — `pr` state is in-memory and resets on reload. (Relevant to the dashboard idea below.)

## Running the preview

The project lives under `~/Desktop`, which is TCC-protected on macOS. The preview
sandbox's system `python3` cannot read it. Use the Node server instead:
`preview_start` with config name `static` (runs `serve.js`). Port 5173. Do not switch
to `python -m http.server`.

## Shipped: offline pass (done)

- ✅ **Truly offline.** Outfit + DM Sans embedded as woff2 data URIs via `embed_fonts.py`. Verified: zero external network requests on load, all 9 font faces load from data URIs. `index.html` is 481 KB.
- ✅ **Favicon** added (monogram as inline SVG data URI).
- ✅ **README.md** written.

## Known gaps / not done

1. **Verify kit diameters (human task).** Used assumed values (15.9 / 20.1 / 22.5 / 26.6 mm). The brief flagged "verify kit sizes"; these affect every Measure comparison. Needs human confirmation against the real kit.
2. **Reflect tab** not built (optional).
3. **Deploy target** not chosen yet (git is initialized locally; no remote / GitHub Pages set up).

## Under discussion: companion analytics dashboard

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
