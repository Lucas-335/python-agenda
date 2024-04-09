from django.contrib import admin
from contacts import models
# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id','first_name','last_name','phone','email','show',
    list_display_links = 'id','first_name'
    list_editable = 'phone','show',
    list_filter = ['last_name']
    ordering = ['-id']
    #list_per_page = 1
    #list_max_show_all =
    search_fields = ['first_name','last_name']

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    
    