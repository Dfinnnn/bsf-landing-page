# PRD — Blue Sky Farms Landing Page (Public Launch)

**Version:** 2.3 (company details from the MoA, new phone contacts, deployment live)
**Date:** 2026-09-25

**What changed from v1.3:** the page is now a **public site at `blueskyfarm.site`**, not an internal demo. The hero switches to the real (wheeled) machine, there is a new headline, a video section, real contact details, a mobile layout, and launch basics.

- v1.3 is archived as `prd_v1.3_archive.md`.
- `design-brief.md` still holds the reasoning; **this PRD wins on any conflict.**

Items marked **PENDING** wait on the video frame report or on an owner confirmation (see §10).

---

## 1. Goal

A visitor on desktop or phone understands within 5 seconds that **Blue Sky Farms builds AI-assisted spraying machines for farms**, and can reach the contact details in one click.

---

## 2. Fixed constraints

| Item | Value |
|---|---|
| Stack | Plain HTML + CSS. No framework, no build step, **no JavaScript** |
| Files | `index.html`, `styles.css`, `assets/` |
| Layout | Desktop design at 1440px (approved). Fluid from 901–1439px. Stacked single column at ≤ 900px |
| Brand name | **Blue Sky Farms** |
| Scope | Technology business only. The land-deal business is not mentioned |
| Hosting | Static host plus the `blueskyfarm.site` domain at Namecheap (§9) |

---

## 3. Decisions log (v2.0 additions; items 1–16 are in the v1.3 archive)

| # | Decision |
|---|---|
| 17 | The real machine is **wheeled** (`Original_Image.jpg`). All tracked-machine images are removed |
| 18 | Hero = `BSF_prototype_image2.png` render. Labels point at the fan misters, the camera and the tablet. The hero overlay Monitor card is removed, because the tablet replaces it |
| 19 | New H1 and subhead from the owner (§4.2) |
| 20 | `Original_Image.jpg` is used in About as a real photo, captioned "Our current prototype", with no concept tag |
| 21 | Video: a 10-second loop in its own section, **not** in the hero (labels can't track a moving machine). Credited to BSF × Farmotic. Goes live only after Farmotic's written OK |
| 22 | Public launch: mobile pass (≤ 900px), fluid 901–1439px, real contact details, launch meta |
| 23 | Contact details = owner-supplied (§4.2). Digits are allowed in the contact section |
| 24 | v1.3 upgrades kept: bento Services, field-map schematic (Services only), S4 reveal, S5 motion |
| 25 | Hero is a split layout: text on the left, the full render in a rounded frame on the right. This is needed for percentage-based labels on a 4:3 image. It stacks below 1100px |
| 26 | Video = FARMO V8 Ginger Plantation 2, 5.0–15.0s, centre-cropped to 4:5 (720×900). V12 is rejected (burned-in performance captions and an editor watermark) |
| 27 | The nav CTA becomes an external link to the EduFarm dashboard login. The hero CTA stays "Talk to our team" → `#contact` |
| 28 | The OG share image stays JPG (social platforms render JPG reliably). The WebP rule applies to on-page images only |
| 29 | BSF co-builds and modifies the FARMO machines with Farmotic. "Builds" in the subhead is accurate; copy is unchanged |
| 30 | The company name, registration number and business address are taken from the MoA (clause 1.1). The location is now Kepong, Kuala Lumpur (replacing Puchong) |
| 31 | Two named phone contacts: Kyle and Sai |
| 32 | Live at blueskyfarm.site via Vercel, deployed from the `site/` folder of the GitHub repo |

---

## 4. Content spec

### 4.1 Page order

1. `nav`
2. `#hero`
3. `#services`
4. `#in-action` (video)
5. `#about`
6. `#contact` (also serves as the footer)

### 4.2 Copy

**Hero** (owner-approved)

| Element | Text |
|---|---|
| H1 | AI-assisted machines, built for real farms. |
| Subhead | Blue Sky Farms builds farm machines designed to work with AI crop-health detection and a simple monitoring dashboard — so what happens in the field is visible, not guessed. |
| CTA (hero) | Talk to our team → |
| Nav CTA | Dashboard login ↗ (opens https://edu-farm-theta.vercel.app/login in a new tab) |
| Image caption | Concept render |

**Hero labels**

The labels are the **only** place the hero says "spraying". They must stay always visible on desktop, and become a list on mobile.

| Text | Points at |
|---|---|
| Mechanised spraying | Fan misters and the spray |
| Built to inspect crop health | Deck camera |
| Designed for at-a-glance monitoring | Tablet in hand |

**Services.** The copy is unchanged from v1.3 (approved), with one fix: the Automate body must **not** say "tracked". Replace "A tracked machine" with "A wheeled machine".

**Video section (`#in-action`)**

| Element | Text |
|---|---|
| H2 | See it in action |
| Descriptor | Our machine at work in the field. |
| Credit | Footage: Blue Sky Farms × Farmotic |

**About.** The copy is unchanged from v1.3 (approved), except "based in Puchong, Selangor" becomes **"based in Kepong, Kuala Lumpur"**. The real-photo caption reads: "Our current prototype".

**Contact** (owner-supplied, real)

- **Company:** BSF Technology Sdn Bhd · Company No. 202501032497 (1633908-U)
- **Address:** No. 42-1, Jalan Prima 2, Pusat Niaga Metro Prima Kepong, 52100 Kuala Lumpur, Malaysia
- **Phone (Kyle):** +60 17-802 6800 → `tel:+60178026800`
- **Phone (Sai):** +60 10-293 3297 → `tel:+60102933297`
- **Email:** blueskyfarms@gmail.com
- **Office hours:**
  - Monday to Friday, 9:00 am to 6:00 pm
  - Saturday, 9:00 am to 12 noon

Each phone number is a `tel:` link and the email is a `mailto:` link. Both are allowed now that the site is public; the "no links" rule was demo-only.

### 4.3 Banned in all copy

- autonomous
- self-driving
- targeted / targeting
- accuracy
- tracked (the machine is wheeled)
- any percentage or performance statistic
- testimonials
- partner logos other than the video credit

### 4.4 Visual tokens

These are unchanged from v1.3: navy `#0B1E3A`, accent `#1ED6EE` used as fill only, light `#F4F7FA`, white, and Manrope.

### 4.5 Image map

| File | Where | Treatment |
|---|---|---|
| `BSF_prototype_image2.png` | Hero | "Concept render" caption |
| Crop of `BSF_prototype_image2.png` (fan misters spraying), **or** a video still if §10 Q1 allows | Automate card | "Concept render" tag if cropped from the render; no tag on a real video still |
| `chili_image.jpg` | Detect card | Unchanged |
| (CSS) | Monitor card | Field-map schematic, per v1.3 §4.6 |
| `Original_Image.jpg` | About, 488px slot (it's a portrait image) | Caption "Our current prototype". No concept tag |
| `human_harvesting.jpg` | About, 800px slot | Unchanged |
| Video clip (PENDING) | `#in-action` | See §4.6 |

**Excluded.** Move these to `_unused/` and never use them:

- `Prototype3.png` and `hero.webp` built from it
- `Prototype2.png`
- `Machine_image.png`
- `BSF_prototype_image.png`
- `Prototype_image.png`
- `harvesting_image.jpg`

The four tracked-machine files are excluded because they show the wrong machine. The other two are excluded for claims, text artifacts, or showing a different machine type.

### 4.6 Video spec

- **Segment:** `FARMO V8 Ginger Plantation 2.mp4`, from 5.0s to 15.0s.
- **Framing:** centre-crop to 4:5 (720×900).
- **Format:** H.264 MP4, 720p, **audio track removed**, ≤ 4 MB.
- **Poster:** a WebP still from the clip, ≤ 150 KB.
- **HTML attributes:** `autoplay muted loop playsinline`, `preload="metadata"`, and the poster set.
- **Reduced motion:** when the OS "reduce motion" setting is on, hide the video and show the poster image instead (CSS only).
- **Launch gate:** the section ships with the `hidden` attribute. Remove it only after Farmotic's written OK (§9 checklist).

---

## 5. MoSCoW

| ID | Feature | Priority |
|---|---|---|
| M1 | Navigation | Must |
| M2 | Hero (new image, headline, labels) | Must |
| M3 | Services (bento, images, field map) | Must |
| M4 | About (real photo pair) | Must |
| M5 | Contact (real details) | Must |
| M6 | CTA scrolls to `#contact` | Must |
| M7 | Layout at 1440 / fluid / mobile | Must |
| M8 | Asset prep | Must |
| M9 | Copy-rule compliance | Must |
| M10 | Video section, built but hidden until the OK | Must |
| M11 | Launch basics (meta, favicon, share preview) | Must |
| S1–S3 | Hover states, asset weight, validity and alt text (as in v1.3) | Should |
| S4 | Scroll reveal | Should |
| S5 | Hotspot pulse and Detect scan line | Should |

---

## 6. Acceptance criteria

Desktop checks run at **1440 × 900**; mobile checks at **375 × 812**; both at 100% zoom.

### M1 — Navigation
- [ ] **Desktop:** logo, 3 links, and 1 CTA.
- [ ] The nav CTA reads "Dashboard login ↗", links to `https://edu-farm-theta.vercel.app/login`, and has `target="_blank" rel="noopener"`.
- [ ] **Mobile:** logo and CTA only; the links are hidden.
- [ ] No hamburger menu and no JavaScript.
- [ ] Each link brings its section into view.

### M2 — Hero
- [ ] **Desktop:** the H1, subhead, CTA and all 3 labels are visible without scrolling.
- [ ] The H1 matches §4.2 exactly.
- [ ] Each label's dot sits on its part: fan misters, deck camera, tablet.
- [ ] The label positions are **percentages of the image box**, so they stay on their parts at 1440, 1280 and 1024 widths.
- [ ] **Mobile:** the image shows first, then the H1, subhead and CTA, then the 3 labels as a list. There are no floating labels.
- [ ] A "Concept render" caption is visible.
- [ ] No tracked-machine image appears anywhere on the page.
- [ ] **Image-failure test** (as in v1.3): text stays legible on `--navy`.

### M3 — Services
- [ ] The bento layout per v1.3 §4.7 on desktop; stacked on mobile.
- [ ] No text says "tracked".
- [ ] The Monitor card uses the field-map schematic, and no grey skeleton bars remain.

### M4 — About
- [ ] `Original_Image.jpg` is shown with the caption "Our current prototype" and no "Concept render" tag.
- [ ] The about copy is 2–3 sentences and says "based in Kepong, Kuala Lumpur". No mention of Puchong anywhere on the page.

### M5 — Contact
- [ ] All details match §4.2 exactly.
- [ ] Both phone numbers are `tel:` links, each labelled with its contact's name (Kyle, Sai). The email is a `mailto:` link.
- [ ] A search of the source for `[` finds no bracket placeholders.
- [ ] No form.

### M6 — CTA
- [ ] The hero CTA scrolls to `#contact` on desktop and mobile.

### M7 — Layout
- [ ] **At 1440:** matches the approved design (split hero per decision 25).
- [ ] **At 1280 and 1024:** no horizontal scrollbar, no overlapping elements, and the hero labels are still on their parts.
- [ ] **At 375:** no horizontal scrollbar, body text ≥ 16px, and every tap target ≥ 44px tall.
- [ ] **At 1920:** content centred, with bands running full width.

### M8 — Asset prep
- [ ] Every on-page image is WebP. The OG image may be JPG.
- [ ] The hero is ≤ 500 KB; every other image is ≤ 200 KB.
- [ ] None of the excluded files is referenced in the page.

### M9 — Copy rules
- [ ] Zero matches in visible copy and alt text for every §4.3 term.
- [ ] Digits appear only in the Contact section and the address.

### M10 — Video
- [ ] The video meets §4.6 (format, size, no audio, poster, attributes).
- [ ] The credit line is visible.
- [ ] With reduced motion on, the poster shows and the video is hidden.
- [ ] Until the launch gate is cleared, the section has the `hidden` attribute and does not appear.

### M11 — Launch basics
- [ ] `<title>` is set, and a `<meta name="description">` of ≤ 160 characters is written in the same honest register as the page.
- [ ] `<meta name="viewport" content="width=device-width, initial-scale=1">` is present.
- [ ] Open Graph title, description and image tags are present. The OG image is a 1200×630 crop of the hero.
- [ ] A favicon is made from the logo's sun mark.
- [ ] `lang="en"`.

### S1–S5
As in the v1.3 archive. S5's hotspot pulse applies to the new hero dots.

### Success criterion
- [ ] 5-second glance test, run twice, once on desktop and once on a phone.
- [ ] Each run: at least 4 of 5 testers name a machine, farms, and AI or automation.

---

## 7. Non-goals

The following are out of scope:

- A dedicated tablet design (tablets get the fluid layout)
- A mobile hamburger menu
- Forms, analytics or JavaScript of any kind
- A video in the hero
- Autoplay with sound
- A Bahasa Melayu version
- Stat blocks, telemetry, detection boxes, confidence numbers (W11)
- Palette or font change (W12)
- JavaScript gimmicks (W13)
- Any mention of the land-deal business
- SEO beyond §M11

---

## 8. Build order (for Claude Code)

1. Asset swap: move the excluded files, then prepare the new hero, Automate crop, About photo, OG image and favicon.
2. Hero rebuild: new image, copy, and percentage-based labels. Remove the overlay Monitor card.
3. Services fixes ("wheeled", new Automate image) and the About photo swap.
4. Contact with the real details.
5. M7: fluid 901–1439, then the ≤ 900 mobile pass.
6. M10 video section, **after** the frame report, left hidden.
7. M11 launch basics.
8. S4 and S5, if not done.
9. Full §6 checklist.

---

## 9. Pre-launch checklist (owner)

- [ ] Namecheap domain contacts verified (**deadline: within 14 days of 2026-09-25**)
- [ ] Farmotic's written OK received, covering both the video and naming Farmotic in the credit line (check the MOA's publicity terms); then remove `hidden` from `#in-action`
- [ ] Boss confirms: AI render images may be shown publicly with the "Concept render" caption
- [ ] Kyle and Sai agree to their names and numbers being on a public site
- [ ] The MoA PDF is never placed in the project folder or the repo (clause 10, confidentiality)
- [ ] Glance test passed on desktop and mobile
- [x] Hosting set up and the domain connected

---

## 10. Open questions

| # | Question | Default |
|---|---|---|
| 4 | The EduFarm homepage copy makes claims this site bans ("instant AI-powered warnings") and uses the name "Blue Sky Farm". Should it be updated? | Out of scope; linking to /login avoids the homepage |
| 2 | Is there a registered company name (Sdn. Bhd.) to show? | "Blue Sky Farms" only |
| 3 | Which static host? | Decided at the deployment step |
