from django.forms import forms
from .models import Author, Tag, Category, Post, Feedback
from django.template.defaultfilters import slugify


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = '__all__'

    def is_valid(self):
        pass

    def save(self):
        pass