from django.contrib import admin

# Register your models here.
from .models import ProfessProfile, Schoolworks


admin.site.register(ProfessProfile)
admin.site.register(Schoolworks)
