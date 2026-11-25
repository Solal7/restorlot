# Restorlot

A map of every department and every job in the property restoration industry, part of City Pretty.
One static page: `index.html` renders everything from `departments.json`. No build step, no cookies.
Preview locally with `python3 -m http.server`, then open http://localhost:8000.
After any edit to `index.html`, run `python3 tools/update-csp.py` to refresh the CSP hashes in `vercel.json`.
