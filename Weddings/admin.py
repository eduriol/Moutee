from django.contrib import admin
from Weddings.models import Wedding, Guest

class GuestInline(admin.TabularInline):
    model = Guest
    extra = 10

class WeddingAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Hosts',   {'fields': ['user1', 'user2']}),
        ('Date',    {'fields': ['date']}),
    ]
    inlines = [GuestInline]
    list_display = ('id', 'date', 'user1', 'user2')
    list_filter = ['date']
    search_fields = ['user1__first_name', 'user1__last_name', 'user2__first_name', 'user2__last_name']
    date_hierarchy = 'date'

admin.site.register(Wedding, WeddingAdmin)