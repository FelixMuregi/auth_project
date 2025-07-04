from django.db import models
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page
from wagtail.images.blocks import ImageChooserBlock
from wagtail import blocks

class HomePage(Page):
    introduction = models.CharField(max_length=250, blank=True)
    body = RichTextField(blank=True)
    cta_link = models.URLField(blank=True)

    content = StreamField([
        ('image_and_text', blocks.StructBlock([
            ('image', ImageChooserBlock(required=True)),
            ('text', blocks.RichTextBlock(required=True)),
        ])),
        ('cta', blocks.StructBlock([
            ('button_text', blocks.CharBlock(required=True, help_text="Text on the button")),
            ('button_url', blocks.URLBlock(required=True, help_text="Link the button should go to")),
        ])),
    ], use_json_field=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduction'),
        FieldPanel('body'),
        FieldPanel('cta_link'),
        FieldPanel('content'),
    ]

