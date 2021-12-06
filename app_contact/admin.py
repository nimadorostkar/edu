from django.contrib import admin
from app_contact.models import Contact, Newsletter


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'created_on']

admin.site.register(Contact, ContactAdmin)





class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['email' , 'created_on']

admin.site.register(Newsletter, NewsletterAdmin)
