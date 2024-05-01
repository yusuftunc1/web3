from django.contrib import admin
from .models import project_page, announcments, about_page, galeri_page

class galeri_page_admin(admin.ModelAdmin):
    list_display = ('display',)
    search_fields = ('display',)
    list_per_page = 20
    list_display_links = ('display',)


class about_page_admin(admin.ModelAdmin):
    list_display = ('confg',)
    search_fields = ('confg',)
    list_per_page = 20
    list_display_links = ('confg',)


class project_page_admin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_per_page = 20
    list_display_links = ('title',)

class announcments_admin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_per_page = 20
    list_display_links = ('title',)


admin.site.register(galeri_page,galeri_page_admin)
admin.site.register(about_page,about_page_admin)
admin.site.register(project_page,project_page_admin)
admin.site.register(announcments,announcments_admin)
# Register your models here.
