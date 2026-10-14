from django.contrib import admin
from django.urls import path
from ruqyah_main.views import landing_page, robots_txt, sitemap_xml, privacy_policy, google_verification

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='landing_page'),
    path('privacy-policy/', privacy_policy, name='privacy_policy'),
    path('robots.txt', robots_txt, name='robots_txt'),
    path('sitemap.xml', sitemap_xml, name='sitemap_xml'),
    path('google1e7b006a43ce6a53.html', google_verification, name='google_verification'),
]
