# Blue Sky Farms — Landing Page (Public Launch)

## Source of truth

- @prd.md — requirements and acceptance criteria (v2.0). **Wins on any conflict.**
- @design-brief.md — the original reasoning. Parts are superseded by PRD v2.0.
- `reference/` — visual references only. Do not copy their copy, brand or stats.
- `assets/` — the images and video used on the page, per PRD §4.5 and §4.6.
- `_unused/` — excluded files. **Never** use anything from here.

## Hard rules

- **Stack:** plain HTML + CSS only (`index.html`, `styles.css`, `assets/`). No framework, no JavaScript, no npm.
- **Layout:** desktop design at 1440px, fluid from 901–1439px, stacked at ≤ 900px (PRD M7).
- **The real machine is WHEELED.** Never show or describe a tracked machine.
- **Copy:** use PRD §4.2 exactly. Do not invent copy, numbers, stats, telemetry, partners or testimonials.
- **Banned words:** see PRD §4.3. Check before finishing any section.
- **Logo:** never recolour or redraw it.
- **Video section:** stays `hidden` until the owner confirms Farmotic's OK.

## Workflow

1. Follow the PRD §8 order.
2. Do one step at a time, then stop and show me (a screenshot plus checklist results) before the next.
3. When something is ambiguous or missing, **ask. Do not assume.**
4. Before calling a step done, run its PRD §6 checks and report pass/fail per item.

## Environment

Windows, PowerShell, VS Code. Preview with `.claude/launch.json` (python http.server).

## Deployment (live)

- **Live site:** https://www.blueskyfarm.site (Vercel). The non-www domain also works.
- **Repo:** github.com/Dfinnnn/bsf-landing-page. Vercel deploys **only the `site/` folder**.
- **Workflow:** edit the root `index.html`, `styles.css` and `assets/` → run `build-site.py` to refresh `site/` → commit → push. Vercel redeploys automatically on push.
- **Never commit:**
  - raw source videos
  - `_unused/`
  - `reference/frames/`
  - any contract or MoA document
- Before pushing, show me `git status` and the list of changed files.
