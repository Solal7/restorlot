# Restorlot v0.1 plan (for approval)

Files: `index.html` (inline CSS and JS), `departments.json` (all content), `vercel.json`. The page fetches `departments.json` and renders every section from it. Local preview: `python3 -m http.server` in the folder.

## Page sections, in order
1. **Top bar.** Wordmark "Restorlot" left; anchor links: The job, Departments, One record, Neighborhoods. Mobile: wordmark plus a menu button.
2. **Hero.** One sentence: "Every department and every job that brings a damaged property back." Buttons: "Follow a job" (scrolls to 3) and "Contact" (scrolls to 7). A small line names the scope: Los Angeles first, sample data marked.
3. **Follow one job.** Fifteen steps of a burst pipe in an older LA house (BRIEF section 4, item 2). Left: a numbered step list (tabs). Right: step name, a short headline, two sentences, the people on site (job titles that link to their department), and a "job record" card that gains one line per step. Prev and Next buttons, arrow keys, no autoplay.
4. **Departments map.** The chain drawn left to right in four stages: Before the call, Emergency, Recovery, Close. Fourteen department tiles sit under their stage; Operations support and Leadership run as a band under all four. Click a tile: a detail panel opens (side panel at 1024px and up, full-width sheet below) listing each job with daily tasks, tools, certifications, key metric, and "hands off to" links that jump to the next department. Search box filters jobs by title.
5. **One job record.** Left: today's scattered tools as generic chips (paper drying logs, photo folders, spreadsheets, group texts, estimating software, accounting software, paper sign-offs). Right: the finished record card from section 3. Copy stays descriptive: this site maps the industry and sells nothing.
6. **Neighborhood layer (placeholder).** A simple parcel-grid drawing with the sample job pinned, plus the five fields City Pretty will read: lat, lng, neighborhood, census tract, year built. One line on why year built matters (pre-1978 lead rules, sourced).
7. **Contact and footer.** Contact email, a line on sources ("every figure links to its source"), a sources list rendered from the JSON, "No cookies" line, City Pretty credit.

## Design direction
- **Feel:** a field notebook and a parcel map. Warm paper, ink lines, thin rules, a faint graph-paper grid in the hero and the map. Distinct from Restomo's white, blue and orange product look.
- **Palette:** paper `#F6F3EC`, panel `#EDE8DC`, ink `#1C2321`, muted ink `#5A6360`, rule `#D9D3C7`. Damage accents used only for damage type: water `#2C6E91`, fire `#B5532A`, mold `#4F6E2E`. Water blue doubles as the link and focus color. Contrast to be checked at 4.5:1 or better in step 3.
- **Fonts:** system stacks only, so nothing external loads. Headings: `Charter, "Iowan Old Style", Georgia, serif`. Body: `system-ui, -apple-system, "Segoe UI", sans-serif`. Data labels and step numbers: `ui-monospace, Menlo, monospace`.
- **Grid:** max width 1200px, 12 columns, 24px gutter, 8px spacing scale. One column under 640px, two columns 640 to 1023px, full layout from 1024px. Works from 320px.
- **Motion:** short fades and the record line sliding in; all off under `prefers-reduced-motion`.
- **Accessibility:** the step list is an ARIA tablist; department tiles are buttons with `aria-expanded`; the panel traps focus while open and closes on Escape; visible focus rings.
- **Security:** `vercel.json` sets CSP `default-src 'self'`, inline script and style allowed by sha256 hash, `connect-src 'self'` for the JSON fetch, plus HSTS, nosniff, frame-ancestors none, referrer and permissions policies.

## departments.json structure
```
meta:        { title, version, scope: "Los Angeles", updated }
stages:      [ { id, name, order } ]                      // before, emergency, recovery, close, support
departments: [ { id, name, stage, summary, why_it_matters, external_parties[],
                 jobs: [ { id, title, daily_tasks[3], tools[], certifications[],
                           key_metric, hands_off_to: [department ids] } ],
                 key_metric, hands_off_to[], source_ids[] } ]
job_steps:   [ { id, order, name, headline, body, department_ids[], job_ids[],
                 record_line: { label, value }, is_sample: true } ]
sample_jobs: [ BRIEF section 6 fields: id, label, damage_type, address, lat, lng,
               neighborhood, census_tract, year_built, is_sample: true ]
sources:     [ { id, title, publisher, url, accessed } ]
```
Rules: every figure carries a `source_ids` entry or stays out; sample data always has `is_sample: true`.

## Placeholder in v0.1
- Sample job location: one LA neighborhood and a 1960s build year, flagged as sample. Address left blank; coordinates at neighborhood level only.
- Neighborhood layer: static drawing and field list, no live map.
- Figures: only the few rules with an official source (EPA RRP pre-1978, OSHA, IICRC course names). Wages, costs and drying times wait for v0.2.
- Contact: a mailto link to an address you choose (open question below).
- Career paths: listed as "coming in v0.2".

## Decisions for you
1. Scope: I planned **Los Angeles first**, as the brief leans that way. OK?
2. Contact email on the site: which address?
3. Hero framing: industry map only (my default) or the start of a product?
