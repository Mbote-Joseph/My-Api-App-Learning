from calendar import c
from re import A
from django.contrib import admin

from restframework.models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'description', 'created_at')
    list_filter = ('name', 'price', 'stock', 'description', 'created_at')
    search_fields = ('name', 'price', 'stock', 'description', 'created_at')
    ordering = ('name', 'price', 'stock', 'description', 'created_at')
    list_per_page = 10
    date_hierarchy = 'created_at'
    fieldsets = (
        ('Book', {
            'fields': ('name', 'price', 'stock', 'description')
        }),
        ('Date information', {
            'fields': ('created_at',)
        }),
    )
    readonly_fields = ('created_at',)
    save_on_top = True
    save_as = True
    save_as_continue = True
    save_on_bottom = True
    actions_on_top = True
    actions_on_bottom = True
    actions_selection_counter = True
    inlines = []
    filter_horizontal = ()
    radio_fields = {}
    prepopulated_fields = {}
    formfield_overrides = {}
    ordering = ('-created_at',)
    list_editable = ('name', 'price', 'stock', 'description')
    list_display_links = ('name', 'price', 'stock', 'description', 'created_at')
    list_display_links_details = False
    list_select_related = ()
    list_per_page = 10
    list_max_show_all = 200
    list_max_show_all_options = 200
    list_editable = ('name', 'price', 'stock', 'description')
    list_display = ('name', 'price', 'stock', 'description', 'created_at')
    list_display_links = ('name', 'price', 'stock', 'description', 'created_at')
    list_display_links_details = False
    list_select_related = ()
    list_per_page = 10
    list_max_show_all = 200

    

admin.site.register(Book)