from django.contrib import admin
from .models import Appointment, BusinessProfile

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'phone', 'date', 'created_at')
    search_fields = ('patient_name', 'phone')
    list_filter = ('date', 'created_at')

@admin.register(BusinessProfile)
class BusinessProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'review_count', 'rating', 'phone')
    
    def has_add_permission(self, request):
        # Prevent creating multiple profiles, restrict to 1
        if self.model.objects.exists():
            return False
        return True
