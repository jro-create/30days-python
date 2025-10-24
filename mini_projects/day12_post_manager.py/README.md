Day 12 Mini Project — Post Manager (forms for create/edit/delete)

Purpose
- Adds form-based Create / Update / Delete views for Post model.

How to integrate (recommended)
1. Copy these files into your blog app:
   - forms.py  -> mini_projects/day12_post_manager/forms.py
   - views.py  -> mini_projects/day12_post_manager/views.py
   - urls.py   -> mini_projects/day12_post_manager/urls.py
   - templates/*copy into day10_blog/blog/templates/blog/*

2. In your project's settings (INSTALLED_APPS), ensure 'blog' is present.
3. In the project-level urls.py (day10_blog/urls.py), include:
   path('', include('blog.urls'))  # ensure this is present
   and then in blog/urls.py include the post-manager urls (or merge them).

4. Run migrations (if you haven't already for Post model):
   python manage.py makemigrations
   python manage.py migrate

5. Start server and visit:
   - /posts/       -> list of posts
   - /posts/new/   -> create post
   - /posts/<id>/edit/ -> edit post
   - /posts/<id>/delete/ -> delete post

Notes
- Templates are basic and intentionally small to focus on Django forms.
- Follow security best practices once you add auth (only authors should edit/delete).

