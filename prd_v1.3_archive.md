# PRD — Blue Sky Farms Landing Page (Concept Demo)

**Version:** 1.3 (adds bento Services layout, field-map schematic, S5 motion)
**Date:** 2026-09-24
**Companion doc:** `design-brief.md` (read it first; this PRD does not repeat its reasoning)

Items marked **PROVISIONAL** are defaults chosen so work can start. Each one has a matching entry in §9 Open Questions.

---

## 1. Goal

A single-page concept landing page. A first-time visitor should understand within 5 seconds that **Blue Sky Farms builds automated, AI-assisted spraying machines for farms**.

---

## 2. Fixed constraints

| Item | Value |
|---|---|
| Stack | Plain HTML + CSS. No framework, no build step, **no JavaScript** |
| Files | `index.html`, `styles.css`, `assets/` |
| Canvas | Fixed 1440px width, desktop only, no RWD |
| Budget | 1 day |
| Brand name | **Blue Sky Farms** (from logo and existing site) |
| Scope | Technology business only. The land-deal business is not mentioned anywhere |

---

## 3. Decisions log

| # | Decision | Source |
|---|---|---|
| 1 | Solutions-company framing; copy says "built to / designed to", no outcome claims | Brief Q1 |
| 2 | Success = 5-second glance test, ≥4/5 pass | Brief Q2 |
| 3 | Audience = general / everyone; hero in plain language | Brief Q3 |
| 4 | Paulvante layout rhythm with BSF palette | Brief Q4 |
| 5 | 3 pillars: Automate / Detect / Monitor | Brief Q5 |
| 6 | Hero = static render `Prototype3.png` with always-visible labels | Brief Q6, Q7 |
| 7 | CTA = anchor scroll to `#contact` | Brief Q8 |
| 8 | Automate label → nozzles; Detect label → crop rows; Monitor → flat UI card, no metrics | R2-Q1 |
| 9 | Address is real; legal name, phone and email are marked placeholders | R2-Q2 |
| 10 | Logo = `Logo_BSF.jpg`, untouched; UI accent is sampled from the logo's cyan | R2-Q3, Q4 |
| 11 | Page is technology-only; land business excluded; Canva contact details not used | R2-Q5 |
| 12 | Stack = plain HTML + CSS | R2-Q6 |
| 13 | Stat blocks and partner strip dropped; non-numeric fact band is a "Could" | R2-Q7 |
| 14 | Sections below the hero fade/slide in on scroll; CSS-only, progressive enhancement | Post-M1 review |
| 15 | Extra images added to Services and About per §4.5; owner confirmed usage; watermarks accepted | Post-M3 review |
| 16 | Design upgrade after external critique: bento Services, field-map schematic replaces skeleton bars, subtle motion (S5). Rejected: palette change, fake telemetry, video, RWD, JS effects, display font | Post-M4 review |

---

## 4. Content spec

### 4.1 Page order

1. `nav`
2. `#hero`
3. `#services` (pillars)
4. `#about`
5. `#contact` (also serves as the footer)

The optional fact band (C1) sits between `#services` and `#about`.

### 4.2 Copy (PROVISIONAL unless stated)

**Hero**

| Element | Text |
|---|---|
| H1 | Automated spraying machines, built for modern farms. |
| Subhead | Blue Sky Farms develops farm spraying machines designed to work with AI crop-health detection and a simple monitoring dashboard. |
| CTA (hero and nav) | Talk to our team → |
| Image caption | Concept render |

**Hero labels**

| Label | Text | Points at |
|---|---|---|
| Automate | Mechanised spraying | Nozzles / spray |
| Detect | Built to inspect crop health | Crop rows |
| Monitor | UI card: title "Farm Monitor" plus a field-map schematic (§4.6) | Beside the machine |

The Monitor card contains **no digits and no measured values**. Its only words are the title and the §4.6 legend labels.

**Pillars**

| Pillar | Line | Body direction (≤40 words each) |
|---|---|---|
| Automate | Spraying, mechanised. | What the machine does. No "autonomous" |
| Detect | Crop health, flagged early. | Vision system is *built to* flag issues; no accuracy claims |
| Monitor | Your farm, at a glance. | Dashboard is *designed to* show farm status; no live-data claims |

**About.** Two to three sentences: Blue Sky Farms is a farm technology team based in Puchong, Selangor. It has no "years of experience" claims and no client counts.

**Contact**
- `[Company Sdn. Bhd.]` (placeholder)
- 21, Jalan SP 3/4, Taman Saujana Puchong, 47100 Puchong, Selangor (**real**)
- `[+60 XX-XXX XXXX]` (placeholder)
- `[email@domain]` (placeholder)

### 4.3 Banned in all copy

- autonomous
- self-driving
- targeted / targeting
- accuracy
- any percentage
- any statistic
- testimonials
- partner logos

### 4.4 Visual tokens (PROVISIONAL)

| Token | Value | Rule |
|---|---|---|
| `--navy` | `#0B1E3A` | Dark bands, text on light bands |
| `--accent` | Sampled from logo cyan (start `#1ED6EE`) | Fills, labels and CTA background only. **Never as text on white** (fails contrast) |
| `--light` | `#F4F7FA` | Light bands |
| `--white` | `#FFFFFF` | Text on navy |

- **Font:** one Google Font family (start with Manrope) with a `system-ui, sans-serif` fallback.
- **Headings:** H2 section headings are uppercase.
- **Radii:** 16px on images and cards; 999px on pills.

### 4.5 Image map

The owner has confirmed these images may be used, and has accepted the watermark risk on the renders.

| File | Where | Treatment |
|---|---|---|
| `Machine_image.png` | Automate card (M3) | Crop to the machine spraying between rows. Add a "Concept render" tag |
| `chili_image.jpg` | Detect card (M3) | Crop to the chili plants |
| (none) | Monitor card (M3) | CSS illustration: the §4.6 field-map schematic at a larger size |
| `Prototype2.png` | About (M4), left of pair | Wide machine shot. Add a "Concept render" tag |
| `human_harvesting.jpg` | About (M4), right of pair | As is, cropped to fit |

**Not used anywhere**, because each shows a *different machine* from the hero and would make visitors ask which one is real:
- `BSF_prototype_image.png` and `BSF_prototype_image2.png` (wheeled robot)
- `harvesting_image.jpg` (tractor boom sprayer)

### 4.6 Field-map schematic (replaces the grey skeleton bars)

Used in two places: the hero Monitor card and the Monitor Services card. It is built in HTML/CSS.

**Structure**
- A small grid of crop-row blocks, drawn as a top-down field view (6–8 rows).
- A few rows are tinted with one of three legend colours; the rest stay neutral.
- A legend below the grid.

**Legend labels**, exactly these three category names:
- Spray plan
- Weather
- Crop checks

**Rules**
- No digits, percentages, units, coordinates or status values (such as "Active" or "Done").
- Row labels, if used, are letters only.
- The legend colours are shades of `--accent` and `--navy`. No new hues.

### 4.7 Services layout (bento)

- **Row 1:** Automate spans 2 of 3 columns with a larger image; Detect takes 1 column.
- **Row 2:** Monitor spans the full width, with the schematic on one side and the text on the other.
- Copy is unchanged.

---

## 5. MoSCoW

| ID | Feature | Priority |
|---|---|---|
| M1 | Navigation bar | Must |
| M2 | Hero section with labels and Monitor card | Must |
| M3 | Services / pillars section | Must |
| M4 | About section | Must |
| M5 | Contact section (CTA target) | Must |
| M6 | CTA anchor-scroll behaviour | Must |
| M7 | Fixed 1440 canvas behaviour | Must |
| M8 | Asset prep (render + logo) | Must |
| M9 | Copy-rule compliance | Must |
| S1 | Hover states on nav links and CTAs | Should |
| S2 | Asset weight budget | Should |
| S3 | Valid HTML + image alt text | Should |
| S4 | Scroll reveal on sections below the hero | Should (built after all Musts pass) |
| S5 | Subtle motion: hotspot pulse, scan line on the Detect image | Should (after S4) |
| C1 | Non-numeric fact band | Could |
| C2 | Favicon from logo sun mark | Could |
| W1–W13 | See §7 | Won't (this version) |

---

## 6. Acceptance criteria

All checks are run at a **1440 × 900 browser window, 100% zoom**, unless stated otherwise.

### M1 — Navigation
- [ ] The nav contains exactly: logo, 3 links (Services, About, Contact), and 1 CTA pill.
- [ ] The logo shows no visible black rectangle against its background.
- [ ] Each link, when clicked, brings its section heading into the viewport.

### M2 — Hero
- [ ] The H1, subhead, CTA, all 3 labels and the Monitor card are visible without scrolling.
- [ ] The H1 contains the words "spraying" and "farms".
- [ ] All label text is real HTML text (selectable), not baked into the image.
- [ ] No label or card requires hover or click to appear.
- [ ] The Automate label's connector ends on the nozzle/spray area.
- [ ] The Detect label's connector ends on a crop row, not on the machine.
- [ ] The Monitor card does not overlap the machine body.
- [ ] The Monitor card contains no digits and no status values; its words are only the title and the three §4.6 legend labels.
- [ ] A "Concept render" caption is visible on or beside the image.
- [ ] **Image-failure test:** with the image path renamed, the hero background is `--navy`, and the H1, subhead and CTA remain readable with contrast ≥ 4.5:1.

### M3 — Services
- [ ] Exactly 3 cards, in order: Automate, Detect, Monitor.
- [ ] The layout matches §4.7: Automate is wider than Detect in row 1, and Monitor spans the full width in row 2.
- [ ] The Monitor card shows the §4.6 schematic, and no grey skeleton bars remain anywhere on the page.
- [ ] Each card has a name, a one-line tagline, and a body of ≤ 40 words.
- [ ] The Detect and Monitor bodies each contain "built to" or "designed to".

### M3 — Services images (§4.5)
- [ ] Each card has one image or illustration above its tagline, matching §4.5.
- [ ] Every image showing the machine carries a visible "Concept render" tag.
- [ ] Each image is WebP and ≤ 200 KB.

### M4 — About
- [ ] Shows the image pair from §4.5, with the machine image tagged "Concept render".
- [ ] 2–3 sentences.
- [ ] Mentions Puchong, Selangor.
- [ ] Contains no numeric claims.

### M5 — Contact
- [ ] The section has `id="contact"`.
- [ ] Shows the real address exactly as in §4.2.
- [ ] The name, phone and email placeholders appear in square-bracket form, findable by searching the source for `[`.
- [ ] No form element exists.
- [ ] Neither Canva phone number appears anywhere in the source.

### M6 — CTA behaviour
- [ ] Clicking either CTA scrolls to `#contact`, and the URL hash becomes `#contact`.
- [ ] The scroll is animated via CSS `scroll-behavior: smooth`.
- [ ] It works with JavaScript disabled.

### M7 — Canvas
- [ ] **At a 1920px window:** content is centred at 1440px, band backgrounds span the full window width, and no white gaps appear at the edges.
- [ ] **At a 1280px window:** a horizontal scrollbar appears and no elements overlap or reflow.

### M8 — Asset prep
- [ ] At 100% zoom on the hero, the render shows no watermark and no readable or scannable QR code.
- [ ] None of the three excluded files in §4.5 is used anywhere.
- [ ] The logo is used with its colours unaltered.

### M9 — Copy rules
- [ ] A case-insensitive search of `index.html` finds zero matches for:
  - `autonomous`
  - `self-driving`
  - `target`
  - `accuracy`
  - `%`
- [ ] Digits appear only in the address and the phone placeholder.

### S1 — Hover states
- [ ] Nav links and both CTAs visibly change on hover (colour or underline).
- [ ] Nothing else on the page has hover behaviour.

### S2 — Asset weight
- [ ] The hero image is ≤ 500 KB (WebP or optimised JPG).
- [ ] Total page weight is ≤ 2 MB.

### S3 — Validity and alt text
- [ ] The W3C validator reports 0 errors.
- [ ] Every `<img>` has non-empty `alt`.
- [ ] The hero image `alt` describes the machine as a concept render.

### S4 — Scroll reveal
- [ ] Implemented in CSS only, inside `@supports (animation-timeline: view())`. No JavaScript.
- [ ] Nav and hero are **not** animated; both are fully visible on page load.
- [ ] Motion is limited to opacity 0 → 1 and an upward slide of at most 24px.
- [ ] **Unsupported-browser test:** with the `@supports` block removed, every element is fully visible and nothing sits at reduced opacity.
- [ ] **Reduced-motion test:** with the OS "reduce motion" setting on, nothing animates and everything is visible.
- [ ] **Bottom-of-page test:** scrolled to the very bottom, every element in `#contact` is at full opacity (not stuck mid-fade because the page can't scroll further).
- [ ] **CTA test:** after clicking a CTA, `#contact` content is at full opacity once scrolling stops.
- [ ] Known behaviour, accepted: the animation is scroll-linked, so scrolling back up reverses it.

### S5 — Subtle motion
- [ ] CSS only. No JavaScript.
- [ ] The hotspot dots pulse (scale and/or glow) on a loop of at least 2 seconds.
- [ ] A single thin accent line sweeps slowly across the Detect image.
- [ ] The Detect image has **no** labels, boxes, rings, text or numbers added. The line is decoration only.
- [ ] **Reduced-motion test:** with the OS "reduce motion" setting on, the pulse and the sweep are both off.
- [ ] Nothing moves in the H1, subhead or CTA.

### C1 — Fact band
- [ ] 3 blocks.
- [ ] No digits except within the location name.
- [ ] Each fact is verifiable from the KB or confirmed by the owner.

### Success criterion (whole page)
- [ ] 5-second glance test per Brief §3: at least 4 of 5 testers (at least 1 non-technical) name a machine or sprayer, farms or agriculture, and automation, AI or robot.

---

## 7. Non-goals (Won't, this version)

- **W1:** Mobile, tablet, or any responsive layout
- **W2:** Forms, submission, WhatsApp or email links, analytics
- **W3:** Video, 3D, carousels, and any animation other than smooth scroll and S4
- **W4:** Bahasa Melayu version
- **W5:** Stat blocks, partner logo strip, testimonials
- **W6:** Any mention of the land-deal business
- **W7:** Login, signup, dashboard embedding
- **W8:** SEO work, meta or OG tuning, deployment
- **W9:** Redesigning or recolouring the logo
- **W10:** Editing any render to add hardware (camera, screen)
- **W11:** Simulated telemetry, detection boxes, confidence scores, or any displayed number that implies measured performance
- **W12:** Palette change away from the logo-derived navy and cyan; display font change
- **W13:** Custom cursor, 3D tilt, magnetic buttons, count-up numbers, ticker marquee

---

## 8. Build and verification handoff (for Claude Code)

1. Put `design-brief.md`, `prd.md`, `Prototype3.png` and `Logo_BSF.jpg` in the repo root before starting.
2. Do asset prep (M8) first. If it can't be done cleanly, stop and flag it rather than proceed with a watermarked render.
3. Build in section order M1 → M5, then M6 and M7.
4. Run §6 as a checklist. The M9 search and the M2 image-failure test are mechanical, so do them, don't eyeball them.
5. C1 and C2 only if everything else passes and time remains.

---

## 9. Open questions

| # | Question | Current default | Blocks |
|---|---|---|---|
| 1 | Final pillar names and copy | Automate / Detect / Monitor, §4.2 | Final copy only |
| 2 | Final H1, subhead and CTA label | §4.2 | Glance-test result |
| 3 | Company legal name, phone, email for the tech business | Bracket placeholders | Any public showing |
| 4 | Transparent PNG/SVG logo available? | Background removal on JPG (shadow edges may be rough) | M1, M8 quality |
| 5 | Exact accent hex and typeface | `#1ED6EE` sample, Manrope | Visual polish only |
| 6 | Usage rights of the AI-generated render for public demos | Unverified; used internally | Any public showing |
| 7 | Where does the QR code on the render resolve? | Blurred regardless | None (resolved by blurring) |
| 8 | Is EverAI a showable partner? | Not shown | Partner strip (W5) |
| 9 | What is the black vertical mast on the machine? | Not labelled | None |
| 10 | Who is on the glance-test panel, and when? | Not set | Success sign-off |
