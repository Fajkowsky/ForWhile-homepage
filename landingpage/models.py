from django.db import models

class ContactModel(models.Model):
    email = models.EmailField()
