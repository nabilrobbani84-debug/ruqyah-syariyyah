from django import forms
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient_name', 'phone', 'date', 'complaint']
        widgets = {
            'patient_name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-forest-green/20 focus:outline-none focus:border-forest-green focus:ring-1 focus:ring-forest-green bg-cream/50',
                'placeholder': 'Nama Lengkap'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-forest-green/20 focus:outline-none focus:border-forest-green focus:ring-1 focus:ring-forest-green bg-cream/50',
                'placeholder': '08xx-xxxx-xxxx'
            }),
            'date': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'w-full px-4 py-3 rounded-lg border border-forest-green/20 focus:outline-none focus:border-forest-green focus:ring-1 focus:ring-forest-green bg-cream/50'
            }),
            'complaint': forms.Textarea(attrs={
                'rows': 4,
                'class': 'w-full px-4 py-3 rounded-lg border border-forest-green/20 focus:outline-none focus:border-forest-green focus:ring-1 focus:ring-forest-green bg-cream/50',
                'placeholder': 'Ceritakan keluhan Anda...'
            })
        }

import urllib.parse
from .models import Appointment, BusinessProfile

def landing_page(request):
    # Fetch or create default business profile
    business = BusinessProfile.objects.first()
    if not business:
        business = BusinessProfile.objects.create(
            name="Ruqyah Syar'iyyah Tanpa Kesurupan",
            therapist_name="Ust. Budi Prastowo",
            address="Jl. H. Anan No.124 RT01 RW07 Pedurenan Bulak, Jatiluhur, Kec. Jatiasih, Kota Bekasi, Jawa Barat 17425",
            phone="0856-9739-7988",
            rating=5.0,
            review_count=415,
            map_embed_url="https://maps.google.com/maps?q=Ruqyah%20Syar'iyyah%20Tanpa%20Kesurupan%20Ust%20Budi%20Prastowo&t=&z=15&ie=UTF8&iwloc=&output=embed"
        )
    
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            
            target_phone = business.phone.replace("-", "").replace(" ", "").replace("+", "")
            if target_phone.startswith("0"):
                target_phone = "62" + target_phone[1:]
                
            message = (
                f"Assalamualaikum Ust. Budi,\n\n"
                f"Saya ingin melakukan reservasi Ruqyah.\n\n"
                f"Nama: {appointment.patient_name}\n"
                f"No. WA: {appointment.phone}\n"
                f"Rencana Tanggal: {appointment.date.strftime('%d-%m-%Y %H:%M')}\n"
                f"Keluhan: {appointment.complaint}\n\n"
                f"Mohon info ketersediaan jadwalnya. Terima kasih."
            )
            encoded_message = urllib.parse.quote(message)
            whatsapp_url = f"https://wa.me/{target_phone}?text={encoded_message}"
            
            messages.success(request, 'Data berhasil disimpan! Mengalihkan ke WhatsApp untuk konfirmasi...')
            return redirect(whatsapp_url)
        else:
            messages.error(request, 'Mohon periksa kembali formulir Anda.')
    else:
        form = AppointmentForm()

    context = {
        'form': form,
        'business': {
            'name': business.name,
            'therapist': business.therapist_name,
            'address': business.address,
            'phone': business.phone,
            'rating': business.rating,
            'reviews_count': business.review_count,
            'map_url': business.map_embed_url or "https://maps.google.com/maps?q=Ruqyah%20Syar'iyyah%20Tanpa%20Kesurupan%20Ust%20Budi%20Prastowo&t=&z=15&ie=UTF8&iwloc=&output=embed"
        }
    }
    return render(request, 'landing.html', context)

from django.http import HttpResponse

def robots_txt(request):
    content = """User-agent: *
Disallow: /admin/
Allow: /

Sitemap: https://ruqyahsyariyyah.com/sitemap.xml
"""
    return HttpResponse(content, content_type="text/plain")

def sitemap_xml(request):
    content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://ruqyahsyariyyah.com/</loc>
    <lastmod>2024-01-20</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>
"""
    return HttpResponse(content, content_type="application/xml")
