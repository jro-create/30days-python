"""
Day 21: API Docs (OpenAPI/Swagger) + CI (GitHub Actions)
--------------------------------------------------------

WHY THIS MATTERS
- API Docs: Frontends and other devs can see and try endpoints without guessing.
- CI: Every push runs tests automatically so broken code never lands on main.

WHAT YOU'LL ADD
1) OpenAPI schema + Swagger UI at:
   - /api/schema/  (machine-readable)
   - /api/docs/    (human-friendly UI + "Authorize" button)
2) GitHub Actions workflow that:
   - Sets up Python
   - Installs your exact deps
   - Runs "python manage.py check" and "python manage.py test"

MENTAL MODEL
- You already have:
  - HTML site (slug routes)
  - DRF read-only API under /api/
  - DRF write API under /api/v1/ with auth + permissions
  - Tests (Day 20)

- Today:
  - Document those endpoints automatically with drf-spectacular
  - Make GitHub run your tests on every push

RUN LOCALLY
- Start server: python manage.py runserver
- Visit docs: /api/docs/

RUN IN CI
- Push to GitHub; check the "Actions" tab for green ✔.

PRO TIPS
- Keep docs in sync by generating schema from your real code (no separate spec file).
- CI should fail loudly when tests break—fix, commit, push again.
"""
print("✅ Day 21 lesson ready — add docs + CI now.")

