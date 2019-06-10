from django.contrib import admin
from .models import Port_domain, Port_detail
# Register your models here.

@admin.register(Port_domain)
class Port_domain_admin(admin.ModelAdmin):
    def show_domain(self):
        return self.domain
    show_domain.short_description = '域名'

    def show_createtime(self):
        return self.createtime
    show_createtime.short_description = '扫描时间'

    list_display = ['pk', show_domain, show_createtime]
    list_filter = ['createtime']
    search_fields = ['domain', 'createtime']
    list_per_page = 5



@admin.register(Port_detail)
class Port_detail_admin(admin.ModelAdmin):
    def show_domain(self):
        return self.domain
    show_domain.short_description = '域名'

    def show_port(self):
        return self.port
    show_port.short_description = '端口号'

    def show_status(self):
        return self.status
    show_status.short_description = '状态'

    def show_reason(self):
        return self.reason
    show_reason.short_description = '原因'

    def show_name(self):
        return self.name
    show_name.short_description = '服务'

    def show_product(self):
        return self.product
    show_product.short_description = '服务供应商'

    def show_version(self):
        return self.version
    show_version.short_description = '版本'

    list_display = ['pk', show_domain, show_port, show_status, show_reason, show_name, show_product, show_version]
    list_filter = ['domain']
    search_fields = ['domain']
    list_per_page = 10