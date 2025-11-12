"""
Day 20: Automated Tests (Django + DRF)
--------------------------------------

WHY TESTS?
- They prove your app works now and keep it from breaking later.
- Recruiters love seeing tests in a junior portfolio.

WHAT YOU'LL TEST TODAY
1) HTML pages load (home + post detail).
2) API (read): list posts, post detail with nested comments, list comments.
3) API (write): creating posts/comments requires auth; owners can edit; others cannot.
4) Permissions: correct HTTP codes (200/201/401/403).

TOOLS
- Django TestCase (built-in) and DRF's APIClient.
- No external server needed; Django runs tests against a temporary test DB.

HOW TO RUN
- All tests:        python manage.py test
- One file:         python manage.py test blog.tests.test_api_read
- One class:        python manage.py test blog.tests.test_api_write.PostWriteAPITests
- One test method:  python manage.py test blog.tests.test_api_write.PostWriteAPITests.test_create_post_requires_auth

SUCCESS SIGNALS
- Green dots + "OK" = good.
- Failures show a traceback with expected vs actual; fix and re-run.

KEEP
- Slug routes stay canonical.
- Read-only endpoints under /api/ (Day 18) remain stable.
- Write endpoints under /api/v1/ (Day 19) use SessionAuth/TokenAuth.
"""
print("✅ Day 20 lesson ready — time to write tests.")

