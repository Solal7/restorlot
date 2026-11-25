# Progress

- 2026-11-24, steps 0 to 2: brief, CLAUDE.md, restomo research notes and PLAN.md done. Plan approved by Solal.
- 2026-11-24, step 3: v0.1 built. index.html, departments.json (14 departments, 61 jobs, 15 steps, 6 official sources), vercel.json (CSP by sha256 hash).
- Checked: served with the vercel.json headers, zero console errors, no sideways scroll at 320, 390 or 1440px, step-through, department panel and job search work.
- Rule: after ANY edit to index.html, run `python3 tools/update-csp.py`, or the live site loses its CSS and JS.
- Preview: `python3 -m http.server` in this folder, then http://localhost:8000. Opening the file directly shows a notice instead.
- 2026-11-25, step 4: content pass. All 14 departments match BRIEF section 5; every job has 3 short tasks; added EPA Section 608 source, cited EPA RRP on the testing step, removed an invented count. Moved to ~/restorlot. Loads with no console errors.
- Next: Solal's review (step 5), then GitHub (6a to 6c), then Vercel import from the Solal7 account (6d).
- Open: contact email (meta.contact_email is empty, site says "coming soon"); industry map vs product; a restoration owner to review section 5.
