"""
Day 23: Image Uploads + Media
-----------------------------

WHY
- Real apps handle files. Recruiters expect you to know MEDIA_URL/ROOT and ImageField basics.

WHAT YOU'LL ADD
1) MEDIA_URL + MEDIA_ROOT in settings, and URLs to serve media in dev.
2) Post.cover (ImageField, optional) with proper migrations.
3) HTML form (multipart) to upload a cover image when creating/editing.
4) DRF API accepts multipart/form-data and returns the cover URL.

HOW TO TEST
- HTML: Create/edit a post, upload an image, see it appear on the detail page.
- API (logged-in): POST /api/v1/posts/ with multipart form including "cover".
- Verify JSON returns "cover": "<http url>" on list/detail.

GOTCHAS
- You *must* set <form enctype="multipart/form-data"> for file uploads.
- Install Pillow or ImageField won’t work.
- For API upload, use multipart/form-data (not JSON).
"""
print("✅ Day 23 lesson ready — set up image uploads.")

