from django.contrib import admin

from . import models
from .models import ContactUs, Author


# Register your models here.
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'date',)
    search_fields = ('name', 'email',)
    date_hierarchy = 'date'


class AuthorAdmin(admin.ModelAdmin):
    pass



admin.site.register(models.ContactUs)
admin.site.register(models.Newsletter)
