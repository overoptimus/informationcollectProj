from django.contrib import admin

# from .models import Url_status, Url, File_ext

from .models import Dir_domain, Dir_detail
# Register your models here.

@admin.register(Dir_domain)
class Dir_domain_admin(admin.ModelAdmin):
    def show_domain(self):
        return self.domain
    show_domain.short_description = '域名'

    def show_file_ext(self):
        return self.file_ext
    show_file_ext.short_description = '文件类型'

    def show_createtime(self):
        return self.createtime
    show_createtime.short_description = '扫描时间'

    list_display = ['pk', show_domain, show_file_ext, show_createtime]
    list_filter = ['createtime']
    search_fields = ['domain', 'createtime']
    list_per_page = 5


@admin.register(Dir_detail)
class Dir_detail_admin(admin.ModelAdmin):

    def show_domain(self):
        return self.domain
    show_domain.short_description = '域名'

    def show_dir(self):
        return self.dir
    show_dir.short_description = '目录'

    def show_status(self):
        return self.status
    show_status.short_description = '状态码'

    list_display = ['pk', show_domain, show_dir, show_status]
    list_filter = ['domain']
    search_fields = ['domain']
    list_per_page = 10

# @admin.register(Url)
# class Url_admin(admin.ModelAdmin):
#     # 列表页属性
#     list_display = ['pk', 'url']
#     list_filter = ['url']
#     search_fields = ['url']
#     list_per_page = 5
#
#     # 添加修改页属性
#     # fields = []
#     # fieldsets = []
#
# @admin.register(File_ext)
# class File_ext_manager(admin.ModelAdmin):
#     # 列表页属性
#     list_display = ['pk', 'file_ext']
#     list_filter = ['file_ext']
#     search_fields = ['file_ext']
#     list_per_page = 5
#
#     # 添加修改页属性
#     # fields = []
#     # fieldsets = []
#
# @admin.register(Url_status)
# class Url_status_manager(admin.ModelAdmin):
#     def url(self):
#         url = Url.obj.get(pk=self.url_id).url
#         return url
#     url.short_description = '域名'
#
#     def dir_path(self):
#         return self.dir_path
#     dir_path.short_description = '目录'
#
#     def status(self):
#         return self.status
#     status.short_description = '状态码'
#     # 列表页属性
#     list_display = ['pk', url, dir_path, status]
#     list_filter = ['status']
#     search_fields = ['status', 'url_id']
#     list_per_page = 5
#
#     添加修改页属性
#     fields = []
#     fieldsets = []
