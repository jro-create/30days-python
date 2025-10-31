"""
Day 13: Django Authentication & User Management
------------------------------------------------

GOAL
- Add registration, login, logout, and a simple profile page.
- Use Django's built-in auth where possible and a small custom form for registration.
- Configure safe redirects and settings.

KEY POINTS (mentor notes)
- Use Django's User model (django.contrib.auth.models.User) for most cases.
- Use UserCreationForm for registration (it handles password hashing).
- Use django.contrib.auth.views.LoginView and LogoutView for standard flows.
- Always use {% csrf_token %} in forms.
- Set LOGIN_REDIRECT_URL and LOGIN_URL in settings.py.
- Redirect after POST to avoid duplicate submissions (Post/Redirect/Get pattern).

COMMON ERRORS
- Forgetting to add 'users' app to INSTALLED_APPS.
- Not including auth URL patterns or wrong template names.
- Templates not located in correct path: blog/templates/ or project-level templates dir.
- Missing LOGIN_REDIRECT_URL in settings -> login redirects to /accounts/profile/ by default.

EXTRA: Security
- Never store raw passwords; Django handles hashing.
- Consider email verification in production.

Quick commands (run in project root)
1. Create app:
   python manage.py startapp users

2. Add 'users' to INSTALLED_APPS in settings.py

3. Add in settings.py:
   LOGIN_REDIRECT_URL = '/'
   LOGIN_URL = 'login'

4. Create URLs and templates (see mini-project starter for exact file contents)

5. Migrate and create superuser:
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser

6. Test:
   python manage.py runserver
   Visit: /register/ , /login/ , /logout/ , /profile/

"""
print("Day 13 lesson: read the file, then follow the mini-project steps.")

