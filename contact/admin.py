from django.contrib import admin
from contact import models

# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', 'show'
    ordering = '-id',
    list_filter = 'created_date',
    search_fields = 'first_name', 'last_name',
    list_per_page = 20
    list_max_show_all = 500
    list_editable = 'first_name', 'last_name', 'show'
    #list_display_links = 'id'

# Register your models here.
@admin.register(models.Category)
class categoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name',
    ordering = '-id',

