# Design Brief — Blue Sky Farm (BSF) Landing Page

**Status:** Draft v1, for review
**Date:** 2026-09-24
**Type:** Designer's concept redesign demo. Not the official site, not a clone of any reference.

---

## 1. Project frame

| Item | Decision |
|---|---|
| Format | Single page, desktop only, fixed 1440px canvas |
| Responsive | None (no RWD) |
| Integrations | None. No backend, no forms that submit, no payments |
| Interaction | Minimal. One anchor-scroll CTA, no other interactive features |
| Build budget | 1 day |
| References | Paulvante Dribbble shot (layout rhythm), faas.com.my (positioning and section logic) |

---

## 2. Positioning — Q1

BSF is presented as a **farm automation and AI integration solutions company**. Its flagship product is an AI-integrated spraying machine, shown through a product render.

**Copy rule (applies to every section).** Capabilities are written as what the system is *built to* or *designed to* do. The following are not allowed anywhere on the page:

- measured outcomes, percentages or accuracy figures
- the words "autonomous" and "self-driving"
- "AI-targeted spraying"

**Why this rule exists.** The KB (`background.md`) states the following about the current product:

- The sprayer is manually driven.
- It sprays continuously and cannot be aimed per plant.
- The vision system is an unvalidated harness with no accuracy data.

A page that implies otherwise contradicts BSF's own documentation.

---

## 3. Success criteria — Q2

The single success measure is the **5-second glance test**.

**Procedure**
- Show the hero at 1440px to 3–5 people for 5 seconds, then hide it.
- Ask: "What does this company do?"
- At least 1–2 people on the panel must be non-technical.

**Pass condition**
- At least 4 of 5 people (or all 3 of 3) answer unprompted with all three of:
  1. a machine or sprayer
  2. farms or agriculture
  3. automation, AI or robot

Visual polish is a standard for the work, not the success measure.

---

## 4. Audience — Q3

The audience is **everyone / general corporate**: farmers, partners, investors, and the public.

**Logged risk.** A page with no primary reader tends to land for no one. The mitigations are:

- The hero uses plain language only. No "digital twin", "IoT", "zero-shot", "computer vision" or similar jargon above the fold.
- Technical terms are allowed below the hero, and only inside pillar detail text.

---

## 5. Visual direction — Q4

The direction is a **hybrid: Paulvante's layout rhythm with BSF's own palette.**

**Taken from Paulvante**
- Alternating dark and light full-width bands.
- Large uppercase section headings, with a short descriptor right-aligned on the same row.
- Pill-shaped navigation, and a pill CTA with an arrow icon.
- Photo grid sections with rounded corners.

**Palette**
- **Deep navy:** dark bands and primary text on light bands.
- **Sky blue:** the *only* UI accent, used for the CTA, labels and active states.
- **White / off-white:** light bands.
- **Green:** comes from photography only and is never used as a UI colour.

**One-accent rule.** No second accent colour is allowed. Blue and green used together as UI colours goes muddy.

**Not decided yet:** exact hex values and typeface. If BSF has existing brand assets, they override this section.

---

## 6. Content scope — Q5

The "8 core features" list is **dropped**. The narrative is built on **3 service pillars**.

| Pillar (working name) | Maps to | Real status per KB | Copy constraint |
|---|---|---|---|
| **Automate** | Spraying machine | Exists: manually driven, continuous spray | "Mechanised / automated spraying". Never "autonomous" |
| **Detect** | Crop health vision | Harness only, accuracy unknown | "Built to flag crop health issues". No accuracy claims |
| **Monitor** | Farm dashboard | Exists as a simulation (digital twin, live weather) | "Designed to give visibility of..." No live-data claims |

**Proposed section order (for review)**

1. Navigation: logo, anchor links, CTA
2. Hero: product render, 3 labels, headline, CTA
3. Pillars: the 3 service pillars
4. About BSF: who BSF is and where it is located
5. Contact / footer: the CTA's target

The Paulvante sections left out are:
- the logo strip, because no confirmed partners exist
- the stat blocks, because no real numbers exist
- the blog grid and FAQ, which don't fit the 1-day budget

The logo strip and stat blocks are tracked as open questions.

---

## 7. Hero technical route — Q6

The hero is a **static render with always-visible callout labels**.

**Image**
- The canonical render is `Prototype3.png` (tracked chassis).
- `BSF_prototype_image.png` is **excluded**, for four reasons:
  - it shows a different machine (wheeled)
  - it carries a fake "AI-Driven Nozzle Targeting" claim
  - it contains "[cite]" text artifacts
  - it shows a third-party brand ("AgroPlot") on the tablet

**Required image prep**
- Remove the watermark in the bottom-right corner.
- Blur or replace the QR code on the tank. Where it resolves to is unknown.

**Labels.** Three labels (Automate / Detect / Monitor) are always visible, with no hover state. They are absolutely positioned over the image.

---

## 8. Edge cases — Q7

| Scenario | Behaviour |
|---|---|
| Visitor never hovers or clicks | Labels are always visible, so there is no information loss |
| Visitor never scrolls | Hero alone states what BSF is, what it makes, and shows the CTA |
| Hero image fails to load | Solid navy background; headline, labels and CTA stay legible |
| Viewport wider than 1440px | Canvas stays centred and band background colours extend full width |
| Viewport narrower than 1440px | Horizontal scroll (accepted, because there is no RWD) |

---

## 9. CTA — Q8

- **Behaviour:** smooth anchor-scroll to the `#contact` section at the bottom of the page.
- **Contact section content:** company name, location and contact details as static text. There is no form.
- **Label wording:** not decided yet.

---

## 10. Non-goals (brief level)

The following are out of scope for this build:

- Mobile or tablet layouts
- Real form submission, WhatsApp or email links
- Login, signup, dashboard embedding
- Video, animation beyond smooth scroll, and any 3D
- Bahasa Melayu version
- Any accuracy, yield or savings figures

---

## 11. Risks

| Risk | Consequence |
|---|---|
| The "everyone" audience dilutes copy | Glance test may pass while sections below the fold lose focus |
| The render is AI-generated and depicts a machine that doesn't exist in that form | A viewer may read it as a real product photo. The page should label it as a concept render |
| The Prototype3 render has no visible camera or screen | The Detect and Monitor labels have no physical part to point at. See open question 1 |

---

## 12. Open questions — to resolve in Round 2

1. **Hotspot anchoring.** `Prototype3.png` shows nozzles, tank and pump, but no camera and no tablet. What do the Detect and Monitor labels point at?
2. **Company facts.** What are BSF's legal name, location and contact details? These are needed for the Contact and About sections.
3. **Brand assets.** Do a BSF logo and brand colours exist?
4. **Pillar names and copy.** Are *Automate / Detect / Monitor* final?
5. **Stat blocks.** Include them with non-numeric facts, or drop them?
6. **Partner strip.** Are there real partners that can be shown (e.g. EverAI)? What is the BSF–EverAI relationship on the page?
7. **Tech stack.** Plain HTML/CSS, Vite + React, or Next.js? This affects the 1-day budget.
8. **Palette and typography.** Exact hex values and typeface.
9. **CTA label.** The wording on the button.
10. **Render usage rights.** Is the AI-generated image cleared for use in a public-facing demo? This is unverified.
