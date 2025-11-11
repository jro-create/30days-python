"""
Day 19: Authenticated Write API (Create/Update/Delete) with DRF
---------------------------------------------------------------

GOALS
- Add write endpoints for your blog using DRF.
- Security model:
  - Read: open to everyone.
  - Write (POST/PUT/PATCH/DELETE): authenticated users only.
  - Ownership: only the post/comment author can edit or delete.
- Support two authentication paths:
  1) SessionAuth (browser) -> requires CSRF token (browsable API handles it).
  2) TokenAuth (CLI/curl) -> send "Authorization: Token <token>" (no CSRF).

PATTERNS
- ViewSets + Router for CRUD.
- Post uses slug as lookup_field; author set from request.user.username.
- Custom permission IsOwnerOrReadOnly (SAFE_METHODS allowed to anyone).
- Keep read-only endpoints under /api/ (Day 18), add write endpoints under /api/v1/ to avoid breaking changes.

CHECKLIST
1) pip install djangorestframework (already), add 'rest_framework.authtoken' + migrate.
2) REST_FRAMEWORK: add DEFAULT_AUTHENTICATION_CLASSES + DEFAULT_PERMISSION_CLASSES.
3) Serializers: separate write serializer for Post (title, content), and Comment write serializer.
4) ViewSets: PostViewSet (lookup by slug), CommentViewSet or custom @action for creating comments on a post.
5) URLs: /api/v1/ mounted with a router; add /api/token-auth/ for token retrieval.
6) Tests:
   - Browser (logged in) -> POST via browsable API works (CSRF handled).
   - curl with token -> Authorization header works without CSRF.
"""
print("✅ Day 19 lesson ready — implement the mini-project.")

