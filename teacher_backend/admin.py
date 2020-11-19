from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(ProfessProfile)
admin.site.register(Schoolworks)
admin.site.register(Grades)
