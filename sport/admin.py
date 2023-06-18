from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

class SeasonTicketAdmin(admin.ModelAdmin):
    list_display=('id','title','description','price','discount','share','is_display','time_create','time_update',)
    list_display_links=('title',)
    search_fields=('title','is_display','time_create','time_update')
    list_filter=('is_display','time_create','time_update')
    ordering=('id','is_display','time_create','time_update')
        
    fields=('title','description','price','discount','share','is_display')
    readonly_fields=('id',)

    actions_on_bottom=True
    list_per_page: 10

class OrderAdmin(admin.ModelAdmin):
    list_display=('id','phone','email','comment','is_dusty','time_create','time_update')
    list_display_links=('email',)
    search_fields=('phone','email','is_dusty','time_create','time_update')
    list_filter=('id','time_create','time_update')
    ordering=('id','is_dusty','time_create','time_update')
        
    fields=('phone','email','comment','is_dusty')
    readonly_fields=('id',)

    actions_on_bottom=True
    list_per_page: 10


admin.site.register(SeasonTicket,SeasonTicketAdmin)
admin.site.register(Order,OrderAdmin)

admin.site.site_header=''
admin.site.site_title=''