from django.db import models

class Appointment(models.Model):
    patient_name = models.CharField(max_length=100, verbose_name="Nama Pasien")
    phone = models.CharField(max_length=20, verbose_name="Nomor WhatsApp")
    date = models.DateTimeField(verbose_name="Tanggal & Jam Booking")
    complaint = models.TextField(verbose_name="Keluhan", help_text="Jelaskan secara singkat keluhan yang dialami")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient_name} - {self.date.strftime('%d %b %Y %H:%M')}"

    class Meta:
        verbose_name = "Pemesanan Jadwal"
        verbose_name_plural = "Daftar Pemesanan"
        ordering = ['-date']

class BusinessProfile(models.Model):
    name = models.CharField(max_length=100, default="Ruqyah Syar'iyyah Tanpa Kesurupan")
    therapist_name = models.CharField(max_length=100, default="Ust. Budi Prastowo")
    address = models.TextField(default="Jl. H. Anan No.124 RT01 RW07...")
    phone = models.CharField(max_length=20, default="0856-9739-7988")
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=5.0)
    review_count = models.IntegerField(default=415, help_text="Update angka ini sesuai Google Maps")
    map_embed_url = models.TextField(blank=True, help_text="Link embed Google Maps")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Pengaturan Bisnis"
        verbose_name_plural = "Pengaturan Bisnis"
