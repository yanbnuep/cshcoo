from django.contrib import admin

# Register your models here.
from .models import CSH, SCOM, Note

admin.site.register(CSH)
admin.site.register(SCOM)
admin.site.register(Note)
