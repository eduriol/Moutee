from django.contrib import admin
from Weddings.models import *



class WeddingAdmin(admin.ModelAdmin):
    fields = ['date', 'user1', 'user2']
admin.site.register(Wedding, WeddingAdmin)

class GuestAdmin(admin.ModelAdmin):
    fields = ['host', 'name', 'surname', 'email']
admin.site.register(Guest, GuestAdmin)

class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'name', 'surname', 'sex', 'email', 'password']
admin.site.register(User, UserAdmin)