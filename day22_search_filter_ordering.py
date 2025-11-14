"""
Day 22: DRF Search + Filter + Ordering
--------------------------------------

WHY THIS MATTERS
- Recruiters expect basic API querying: search text, filter by fields, and sort results.
- Frontends need this so they don't pull everything and filter on the client.

WHAT YOU'LL ADD
- /api/v1/posts/?search=hello         -> matches title/content/author
- /api/v1/posts/?author=owner         -> filter by author
- /api/v1/posts/?ordering=-date_posted -> newest first (default) or +title, -title, etc.
- /api/v1/comments/?post__slug=...    -> filter comments by post slug

TOOLS
- django-filter (server-side filtering)
- DRF SearchFilter + OrderingFilter

MENTAL MODEL
- Filter is exact/field-based (e.g., author=owner).
- Search scans text fields (title/content/author).
- Ordering sorts results (date_posted, title, author).

HOW TO TEST
- Browser: /api/v1/posts/?search=blog
- curl:   curl -s "http://127.0.0.1:8000/api/v1/posts/?ordering=title" | python -m json.tool

KEEP
- Existing auth/permissions unchanged.
- Comments action still uses the correct serializers (Day 19 fix).
- Pagination stays at PageSize=5 (Day 18).
"""
print("✅ Day 22 lesson ready — implement filters/search/order now.")

