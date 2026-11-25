# Progress

- 2026-11-24, steps 0 to 2: brief, CLAUDE.md, restomo research notes and PLAN.md done. Plan approved by Solal.
- 2026-11-24, step 3: v0.1 built. index.html, departments.json (14 departments, 61 jobs, 15 steps, 6 official sources), vercel.json (CSP by sha256 hash).
- Checked: served with the vercel.json headers, zero console errors, no sideways scroll at 320, 390 or 1440px, step-through, department panel and job search work.
- Rule: after ANY edit to index.html, run `python3 tools/update-csp.py`, or the live site loses its CSS and JS.
- Preview: `python3 -m http.server` in this folder, then http://localhost:8000. Opening the file directly shows a notice instead.
- 2026-11-25, step 4: content pass. All 14 departments match BRIEF section 5; every job has 3 short tasks; added EPA Section 608 source, cited EPA RRP on the testing step, removed an invented count. Moved to ~/restorlot. Loads with no console errors.
- 2026-11-25, step 6a: git init in ~/restorlot, repo-only identity schasques@gmail.com, first commit 8163c1b on main. BRIEF.md, CLAUDE.md and research/ are gitignored (private). Vercel account confirmed: Solal7 only.
- 2026-11-25, step 6: pushed to Solal7/restorlot; deployed by Solal on Vercel under the Agental team (his choice, transfer to a Solal7 scope later). Live: https://restorlot.vercel.app/
- 2026-11-25, v0.2: plainer hero, "Start here" strip and glossary, LA demo (Beverly Hills 90210, Boyle Heights 90033, South LA 90011) from ACS 2020-2024 via Census Reporter and Census Gazetteer center points; step 1 switches to tenant when most homes are rented. Tested at 320/390/1440, no console errors. Census API now needs a key; Census Reporter needs none.
- Open: cookies (site promises none; asked Solal what they are for), contact email.
- Open: contact email (meta.contact_email is empty, site says "coming soon"); industry map vs product; a restoration owner to review section 5.
