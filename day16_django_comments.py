"""
Day 16: Comments — Nested CRUD with Ownership & Messages
-------------------------------------------------------

YOU'LL BUILD
- A Comment model linked to Post (FK, cascade delete).
- Create & Delete for comments using CBVs.
- Auto-assign comment author from the logged-in user.
- Show comments under each post + a form to add new comments.
- Enforce ownership: only the comment author OR the post author can delete.

MENTAL MODEL
- Post : Comment = 1 : many (ForeignKey with related_name='comments').
- Use ModelForm for comment content (author set in the view).
- Use LoginRequiredMixin for create/delete; add a test for delete.
- Redirect back to the post detail after actions.
- Reuse messages framework for success/error feedback.

WHY THIS MATTERS
- “Child resources” are everywhere (reviews, replies, todos in a project).
- You’re learning how to pass a parent pk in the URL and wire success_url dynamically.

NEXT
- Slugs, richer templates, and API with DRF.
"""
print("✅ Day 16 lesson ready — implement the mini-project steps in the blog app.")

