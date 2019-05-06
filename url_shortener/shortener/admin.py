from django.contrib import admin
from .models import UrlModel

class UrlModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'original_url', 'shortened_url', 'url_slug', 'date_added')
    list_display_links = ('original_url',)

admin.site.register(UrlModel, UrlModelAdmin)
