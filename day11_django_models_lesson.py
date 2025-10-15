"""
Day 11: Django Models & Database Setup

🎯 GOAL:
Learn how Django interacts with databases through its ORM (Object Relational Mapper) 
and how to create, migrate, and view data using models.

📘 THEORY SECTION:
- Django models map Python classes to database tables.
- Each attribute in a model becomes a field (column) in your database.
- Migrations track and apply database schema changes.
- The admin interface allows data management through a GUI.

🧩 PRACTICAL STEPS:

1️⃣ Create a new app:
    python manage.py startapp members

2️⃣ Add 'members' to settings.py:
    INSTALLED_APPS = [
        ...
        'members',
    ]

3️⃣ Define a model in models.py:
    from django.db import models

    class Member(models.Model):
        first_name = models.CharField(max_length=50)
        last_name = models.CharField(max_length=50)
        email = models.EmailField()
        joined_date = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f"{self.first_name} {self.last_name}"

4️⃣ Make and apply migrations:
    python manage.py makemigrations
    python manage.py migrate

5️⃣ Register model in admin.py:
    from django.contrib import admin
    from .models import Member
    admin.site.register(Member)

6️⃣ Run server and access admin:
    python manage.py runserver
    Visit: http://127.0.0.1:8000/admin

🧠 CONCEPT RECAP:
✔ Models = Database structure in Python
✔ makemigrations = Prepare changes
✔ migrate = Apply changes
✔ Admin = GUI to manage data
"""

