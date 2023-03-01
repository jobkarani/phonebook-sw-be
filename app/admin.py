from django.contrib import admin

from app.models import *

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'email', 'phoneNumber', 'profilePicture', 'location')
    prepopulated_fields = {'slug': ('firstName',)}

admin.site.register(Contact, ContactAdmin )