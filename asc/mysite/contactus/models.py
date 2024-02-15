from django.db import models


# Create your models here.
# ...

class ContactUs(models.Model):
    name = models.CharField(max_length=200, help_text="Name of the sender")
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Feedback"

    def __str__(self):
        return self.name + "   - email is -   " + self.email


class Newsletter(models.Model):
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.email


class Author:
    pass


class Tag:
    pass


class Category:
    objects = None


class Post:
    pass


class Feedback:
    pass
