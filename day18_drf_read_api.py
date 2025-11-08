"""
Day 18: Read-Only API with Django REST Framework (DRF)
------------------------------------------------------

GOALS
- Add a JSON API for your blog without breaking your HTML site.
- Endpoints (read-only):
  - GET /api/posts/                 -> list posts (paginated)
  - GET /api/posts/<slug>/          -> post detail (with nested comments)
  - GET /api/posts/<slug>/comments/ -> list comments for a post
  - GET /api/comments/<id>/         -> single comment detail (optional)

WHY THIS MATTERS
- Almost every junior role touches APIs. Being able to expose clean read endpoints
  with pagination and stable identifiers (slugs) is employable, timeless knowledge.

PATTERNS (KEEP THEM)
- Canonical URLs use slugs; legacy pk routes redirect (web).
- API versioning via a top-level prefix (here: /api/; easy to switch to /api/v1/ later).
- Consistent serializers; minimal permissions for read-only (AllowAny).
- Pagination baked into settings to avoid massive payloads.

CHECKLIST
1) pip install djangorestframework
2) settings: add 'rest_framework' to INSTALLED_APPS; set pagination in REST_FRAMEWORK.
3) serializers: PostSerializer (with nested comments), CommentSerializer.
4) views: Read-only List/Detail views for Posts and Comments.
5) urls: /api/ prefix with clearly named routes.
6) curl tests: verify 200s, pagination keys, and nested comments in detail.

Next steps after Day 18:
- Day 19: write endpoints (auth needed) + CSRF matters
- Day 20: API tests with pytest or Django test client
"""
print("✅ Day 18 lesson ready — time to implement the API.")

