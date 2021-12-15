from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index





class IndexPage(Page):
    body = RichTextField()


class BlogPage(Page):
    body = RichTextField()
    

    

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
    ]

    search_fields = Page.search_fields + [
        index.SearchField('body')
    ]

class ContactPage(Page):
    body = RichTextField()


class Contact(models.Model):
    name = models.TextField()
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email