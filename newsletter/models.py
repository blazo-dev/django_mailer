from django.db import models as m

# Create your models here.


class NewsletterUser(m.Model):
    email = m.EmailField(null=False, unique=True)
    date_added = m.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.email)


class Newsletter(m.Model):
    subject = m.CharField(max_length=250)
    name = m.CharField(max_length=250)
    body = m.TextField(blank=True, null=True)
    email = m.ManyToManyField(NewsletterUser)
    created = m.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
