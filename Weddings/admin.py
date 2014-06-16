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

admin.site.register(Wedding, WeddingAdmin)