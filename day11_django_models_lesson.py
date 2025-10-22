"""
Day 11: Django Models & Admin Mastery
-------------------------------------
This lesson introduces how Django handles databases through models,
how to make migrations, and how to manage data in the admin interface.
"""

# 🧠 What are Models?
# Models are Python classes that represent tables in your database.
# Each model defines the structure of your data — fields and their types.

# 🗃️ Example model (in blog/models.py):
# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     date_posted = models.DateTimeField(auto_now_add=True)
#     author = models.CharField(max_length=50)
#
# Each class variable (like title, content) becomes a column in your table.

# 🧩 ORM (Object Relational Mapper):
# Lets you query the database with Python code instead of SQL.
# Example:
#   Post.objects.all()
#   Post.objects.filter(author='Juan')
#   Post.objects.create(title="My Post", content="Hello World!")

# ⚙️ Django commands for models:
#   python manage.py makemigrations   -> Prepare migration files
#   python manage.py migrate          -> Apply changes to the database
#   python manage.py createsuperuser  -> Create admin login
#
# Admin Panel: http://127.0.0.1:8000/admin/

print("✅ Django Models & Admin: Lesson complete.")

