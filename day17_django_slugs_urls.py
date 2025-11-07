"""
Day 17: Slugs & Nicer URLs (with Backward Compatibility)
--------------------------------------------------------

GOALS
- Add a 'slug' (URL-safe identifier) to Post and auto-generate from title.
- Use slug-based routes for detail/edit/delete, e.g. /posts/my-first-post/
- Keep old pk-based URLs working (redirect or alias) so nothing 404s.
- Handle collisions (same title) by appending a short suffix.

WHY IT MATTERS
- Human-readable URLs improve UX and SEO.
- Stable identifiers (slugs) decouple URLs from database IDs.
- Employers expect you to think about backward compatibility.

PATTERN
- models.Post.slug = SlugField(unique=True, blank=True)
- override save(): if no slug, slugify(title); if exists, append "-xyz"
- views: set slug_field = "slug", slug_url_kwarg = "slug"
- urls: /posts/<slug:slug>/, plus legacy /posts/<int:pk>/ -> redirect to slug

CHECKLIST
1) Add slug to model + helper to ensure uniqueness.
2) Update admin to show slug + prepopulate.
3) Update CBV routes to use slug.
4) Keep old pk routes as 301 redirects.
5) Update templates to link by slug.
6) Migrate; test legacy and new URLs.

Next steps later:
- Auto-regenerate slug on title change (optional)
- Add unique constraints with custom validation
- Add canonical link headers
"""
print("✅ Day 17 lesson ready — implement the mini-project steps.")

