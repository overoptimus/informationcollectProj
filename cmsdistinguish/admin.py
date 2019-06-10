from django.contrib import admin
from .models import Cms

# Register your models here.
@admin.register(Cms)
class Cms_admain(admin.ModelAdmin):
    def show_domain(self):
        return self.domain
    show_domain.short_description = '域名'

    def show_cmstype(self):
        return self.cmstype
    show_cmstype.short_description = 'CMS类型'

    list_display = ['id', show_domain, show_cmstype]
    list_filter = ['domain']
    search_fields = ['domain']
    list_per_page = 10