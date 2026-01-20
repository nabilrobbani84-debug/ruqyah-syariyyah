import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ruqyah_project.settings')
django.setup()

from django.contrib.auth.models import User

username = "Nabil Robbani"
password = "Faqih123_"
email = "nabil@example.com"

# Check if user exists
if User.objects.filter(username=username).exists():
    print(f"User '{username}' already exists. Updating password...")
    user = User.objects.get(username=username)
    user.set_password(password)
    user.is_staff = True
    user.is_superuser = True
    user.save()
    print("Password updated successfully.")
else:
    print(f"Creating superuser '{username}'...")
    User.objects.create_superuser(username, email, password)
    print("Superuser created successfully.")
