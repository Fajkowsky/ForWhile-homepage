from django.contrib import admin
from models import ContactModel

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'email',)

admin.site.register(ContactModel, ContactAdmin)