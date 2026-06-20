import os
import django
import shutil

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ruqyah_project.settings')
django.setup()

from django.test import Client
from django.conf import settings

client = Client()

public_dir = os.path.join(settings.BASE_DIR, 'public')
if os.path.exists(public_dir):
    shutil.rmtree(public_dir)
os.makedirs(public_dir)

# landing
res_landing = client.get('/')
with open(os.path.join(public_dir, 'index.html'), 'wb') as f:
    f.write(res_landing.content)
print(f"Landing page generated: {len(res_landing.content)} bytes")

# privacy policy
privacy_dir = os.path.join(public_dir, 'privacy-policy')
os.makedirs(privacy_dir, exist_ok=True)
res_privacy = client.get('/privacy-policy/')
with open(os.path.join(privacy_dir, 'index.html'), 'wb') as f:
    f.write(res_privacy.content)
print(f"Privacy Policy generated: {len(res_privacy.content)} bytes")

# robots & sitemap
res_robots = client.get('/robots.txt')
with open(os.path.join(public_dir, 'robots.txt'), 'wb') as f:
    f.write(res_robots.content)

res_sitemap = client.get('/sitemap.xml')
with open(os.path.join(public_dir, 'sitemap.xml'), 'wb') as f:
    f.write(res_sitemap.content)

# Copy static files
static_source = os.path.join(settings.BASE_DIR, 'static')
static_dest = os.path.join(public_dir, 'static')
if os.path.exists(static_source):
    shutil.copytree(static_source, static_dest)
    print("Static files copied successfully.")
else:
    print("No static files found.")
