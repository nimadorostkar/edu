from django.contrib import admin
from app_contact.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'created_on']

admin.site.register(Contact, ContactAdmin)
