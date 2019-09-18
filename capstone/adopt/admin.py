from django.contrib import admin
from .models import Adopt
# Register your models here.
admin.site.register(Adopt)
class AdoptAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'breed', 'description', 'image',
        'years_old', 'location',)

    readonly_fields = (
        'created',
        'modified',
        'posted_by',
    )