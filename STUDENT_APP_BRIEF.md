# Hydraulic Force Lab — Student App (Day 1 companion)

> **Handoff brief.** This is a self-contained spec for a *new* app, written to be picked up by a
> fresh Claude Code session with no memory of how it was created. Everything you need is here.
> It is a sibling to, not part of, the existing **Hydraulic Rescue Arm Teacher Guide** (that guide
> is the teacher-facing deliverable; this is the student-facing one).

---

## 1. What this is

A single-file, **offline**, web app that students use during **Day 1** of the TETC (ExxonMobil
Foundation · Teen Engineering + Tech Center) **Hydraulic Rescue Arm** unit. It makes the abstract
force/distance + area-ratio physics something teens can play with, predict with, and measure their
real lab data against.

It **augments**, never replaces, the hands-on syringe lab. The loop is: *play with it → predict →
go measure the real syringes → compare → see the gap.*

The one idea the whole app serves:
> **Force and distance are a single budget. The area ratio — the square of the diameter ratio —
> decides how the budget is spent. And the ideal equation always loses a little to friction, seal
> drag, and air in the line. Engineering lives in that gap.**

## 2. Audience & setting

- **Users:** students ~grades 7-10, working in pairs at lab stations.
- **Devices:** school laptops / Chromebooks (Chrome), sometimes projected. Touch and mouse both.
- **No accounts, no network, no data collection.** Runs fully offline from a single file. Any saved
  data stays on the device (localStorage only). This is a school setting: privacy-safe by design.

### Day 1 context (so the content lands right)
Day 1 ("From Syringes to Systems", 90 min) runs **Engage → Design → Build → Evaluate**. This app
serves the **Engage** arc:
1. Feel force vs distance with two pre-connected syringe pairs (one 1:1, one small-to-big), measure
   force and distance, record observations.
2. Name the physics: **Pascal's Principle** (pressure in a confined fluid transmits equally).
3. Reason it: a wider output piston has more area, so more force; area grows with the **square** of
   diameter, so a little wider is a lot stronger; what you gain in force you pay back in distance.
4. Prove it: **force multiplier = (output diameter / input diameter)²**.
5. Practice on escalating ratio problems.
6. Verify: compare the predicted multiplier to what they measured. It never matches exactly. The
   teacher guide dramatizes this as **4.0× predicted vs 3.2× measured — a 0.8× gap** from friction,
   seal drag, air, and inconsistent hand force.

## 3. Core features (MVP — scope tightly to Day 1)

Three tabs in one page: **Explore · Measure · Practice**. (Optional 4th: Reflect.)

### Tab 1 — Explore (the simulator)
The free-play sandbox for the area-ratio idea.
- **Inputs:** choose an **input** syringe and an **output** syringe (diameter). Offer preset buttons
  for the real kit sizes AND a free slider/number entry. (Verify kit sizes; sensible standard inner
  diameters: 10 mL ≈ 15.9 mm, 20 mL ≈ 20.1 mm, 30 mL ≈ 22.5 mm, 60 mL ≈ 26.6 mm.)
- **Live readouts:**
  - Force multiplier = (d_out / d_in)², shown big.
  - Distance multiplier = its inverse (output moves 1/N as far).
  - Plain-language line: e.g. "Push with 1 unit of force, get 4 out. Push 4 cm in, get 1 cm out."
- **Two visuals:**
  - **Area circles:** two filled circles sized by diameter, with their areas labeled, to make the
    *squared* relationship visible (double the diameter → 4× the area).
  - **Syringe animation:** press a "Push" button; the input plunger travels a set distance, the
    output plunger moves the scaled (smaller) distance while a weight/arm lifts. Force arrows scale
    with the multiplier. This is where "force up, distance down" becomes felt, not just stated.
- **Config callouts** mirroring the unit's three cases: 1:1 (trade nothing), small-to-big (more
  force, less travel), big-to-small (more travel/speed, less force).

### Tab 2 — Measure (predict → record → compare → the gap)
The heart of the app; ties to the Verify beat.
- Student selects/enters their **syringe pair** → app shows the **predicted** multiplier.
- Student enters what they **measured** at the bench (keep it simple: e.g. input force and output
  force from spring/kitchen scales, OR input distance and output distance). App computes the
  **measured** multiplier.
- **The gap visual:** two horizontal bars, "Equation predicts N.N×" vs "You measured M.M×",
  exactly like the teacher guide's gap viz, with the difference called out and a prompt: *"Where did
  the missing force go? Name three places a real system leaks, rubs, or compresses."* (friction,
  plunger seal drag, air in the line, inconsistent hand force).
- **Lab log:** each comparison can be saved to a small table (pair, predicted, measured, gap, notes)
  persisted in localStorage. Add/clear rows. This is their record for the notebook/Evaluate step.

### Tab 3 — Practice (quick challenges)
3-6 short, auto-checked problems escalating from calculation to design choice. Examples:
- "An input is 16 mm, output 32 mm. What is the force multiplier?" (→ 4×)
- "You need to lift 4× harder. Pick a pair that does it." (multiple choice of diameter pairs)
- "Your robot needs to reach far and fast, not lift heavy. Big-to-small or small-to-big?"
- "Double the output diameter. Does force double?" (→ no, it quadruples — the square)
Give immediate, constructivist feedback (nudge with a question, then confirm), not just right/wrong.

### Tab 4 — Reflect (OPTIONAL, low priority)
Capture the Day 1 notebook prompts digitally (saved locally): "What are you most sure about? What
are you still figuring out? What is the first thing you do tomorrow?" Skip if time-boxed.

## 4. Math & data model

```
multiplier      = (d_out / d_in) ** 2          // force multiplier (ideal)
distanceFactor  = 1 / multiplier               // output travel vs input travel
measuredMult    = outputForce / inputForce     // from measured forces
                = distanceIn / distanceOut      // (equivalent, from distances)
gap             = predictedMult - measuredMult  // always >= ~0 in practice
efficiency      = measuredMult / predictedMult  // optional, as a %
```
- Work in consistent units; diameter ratio is unitless so mm or inches both fine if consistent.
- Guard against divide-by-zero and nonsense input (d_in = 0, negative, output < input where the UI
  implies otherwise). Round displays to 1 decimal; keep full precision internally.
- **localStorage keys** (namespace to avoid clashes): `hfl:log` (JSON array of rows),
  `hfl:reflect` (JSON), `hfl:lastPair` (JSON). Wrap reads in try/catch.

## 5. Design system — MATCH the teacher guide

Keep this visually consistent with the existing guide so it feels like one unit. Tokens:
- **Palette:** TEAL `#186172`, TEAL_DARK `#134E5C`, TEAL_DEEP `#0f4651`, TEAL_SOFT `#E1EDEE`,
  TURQUOISE `#0DB4AE` (the logo's "Teen Engineering" arrow) + soft `#E2F5F3`, MAGENTA `#BD2F7F` +
  soft `#f7e6ef`, GOLD `#F0C896`, ORANGE `#E8943A`, ORANGE_TEXT `#B87A2A`, WARM_BG `#F7F3EF`,
  PAPER `#ffffff`, INK `#333333`, INK_SOFT `#5a5a5a`, INK_FAINT `#8a8a8a`, RULE `#e6ddd4`.
- **Fonts:** Outfit (headings, variable weight) + DM Sans (body). Embed as woff2 data URIs for
  offline; system-font fallbacks. (The teacher-guide repo has both fonts under `assets/fonts/`.)
- **Logos:** square TE+TC mark in a top bar; full lockup in a footer. (In teacher-guide repo under
  `assets/logos/`: `tetc-mark.png`, `tetc-logo.png`.) Favicon = the square mark.
- **Accent meaning (reuse from the guide):** teal = primary/opener, magenta = the headline/answer,
  orange = build/do, turquoise = check/close. The gap-vs-measured visual should echo the guide's:
  predict bar in teal, measured bar shorter, the difference in orange.
- **Voice rules (non-negotiable, same as the guide):** NO em-dashes (use `·` or commas). NO bullet
  points in student copy (use numbered lists, chips, or slash-bullets `/`). Action-led, plain,
  encouraging. Short sentences. Talk to a teen, not down to them.

## 6. Tech constraints

- **One self-contained `index.html`.** All CSS in a `<style>`, all JS in a `<script>`, fonts/logos
  as base64 data URIs. No CDN, no external requests, no build step required at runtime.
- **Vanilla JS** (no framework, no npm deps). Visuals via inline **SVG** (preferred) or `<canvas>`.
- **Offline-first**, works opened via `file://` or served statically. **No `Date.now()`/random gating**
  needed; if used, keep deterministic where it matters.
- **Accessible & classroom-friendly:** large tap targets (44px+), high contrast, keyboard usable,
  readable at projector distance, responsive down to a small Chromebook window.
- **Resilient input:** never crash on weird numbers; show gentle guidance instead.
- Size target: keep it light (well under a few MB even with embedded fonts/logos).

### Build approach (recommended)
This app has little media, so a **single hand-authored `index.html`** is simplest — no generator
needed. (The teacher guide uses a `build.py` that inlines assets and emits `index.html`; only adopt
that pattern here if asset-inlining gets unwieldy. Don't over-engineer.) If you do embed fonts/logos,
a tiny `build.py` that base64-inlines them into a template is fine, but optional for MVP.

## 7. Suggested structure & milestones

```
hydraulic-force-lab/
  index.html          # the deliverable (self-contained)
  assets/             # source fonts/logos if you inline at build time (else embed directly)
  build.py            # OPTIONAL, only if inlining assets from a template
  README.md           # this brief, trimmed to a real project readme
```
Milestones:
1. Shell + tabs + design tokens + top bar/footer matching the guide.
2. **Explore** tab: diameter inputs, multiplier math, area-circles SVG, push animation.
3. **Measure** tab: predict → enter measured → gap bars → save to localStorage log.
4. **Practice** tab: 3-6 challenges with constructivist feedback.
5. Polish: responsive, accessibility, empty/error states, favicon. (Reflect tab if time.)

## 8. Acceptance criteria (definition of done)

- Opens offline from a single file; no network requests; works in Chrome on a Chromebook.
- Explore: changing either diameter updates the multiplier, the inverse-distance, the area circles,
  and the animation correctly; the squared relationship is visually obvious.
- Measure: predicted vs measured renders as the gap visual; saving/clearing log rows persists across
  reloads; bad input is handled gracefully.
- Practice: every challenge checks an answer and gives feedback.
- Visually consistent with the teacher guide (palette, fonts, voice). No em-dashes, no bullets in
  student copy.
- Readable and operable by a 7th grader without instruction.

## 9. Out of scope (don't build for v1)

- Full hydraulic-arm / multi-joint design simulator (that competes with the real Day 1 build).
- Day 2 / Day 3 content, the relay race, accounts, class dashboards, teacher analytics, cloud sync,
  multiplayer. Keep it a single-student/pair tool for Day 1 Engage.

## 10. Visual reference

- **Live teacher guide:** https://tetc-edu.github.io/Hydraulic-Arm-Teacher-Guide/ (study the look:
  topbar mark, section bands, callout styles, and especially the **gap visual** on Day 1 / Reference,
  which this app's Measure tab should echo).
- **Teacher-guide repo:** https://github.com/TETC-Edu/Hydraulic-Arm-Teacher-Guide — `build.py` holds
  the exact palette in `:root`, the embedded fonts under `assets/fonts/`, and logos under
  `assets/logos/`. Pull tokens/assets from there for a seamless match.

---

### Note on the gap visual to copy
The teacher guide renders the gap as two stacked horizontal bars: a full-width "Equation predicts
4.0×" bar (teal) and a shorter "Students measure 3.2×" bar, with a caption naming the 0.8× gap as
friction / seal drag / air / inconsistent hand force. Reproduce that feel in **Measure**, but driven
by the student's own entered numbers.
