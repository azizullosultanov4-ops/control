from django.contrib import admin
from apps.core.models import Control
# Register your models here.
@admin.register(Control)
class ControlAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'phone', 'email', 'locate', 'logo']
    search_fields = ["title"]