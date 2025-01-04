from typing import ClassVar

from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel


class HeroMixin(models.Model):
    """
    Mixin to add a hero section to a page."""

    hero_title = models.CharField(max_length=255, blank=False)
    hero_subtitle = models.CharField(max_length=255, blank=True)
    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,
        blank=False,
    )
    hero_image_alt_text = models.CharField(max_length=255, blank=False)

    hero_panels: ClassVar[list[MultiFieldPanel]] = [
        MultiFieldPanel(
            [
                FieldPanel("hero_title"),
                FieldPanel("hero_subtitle"),
                FieldPanel("hero_image"),
                FieldPanel("hero_image_alt_text"),
            ],
            heading="Hero Section",
        )
    ]

    class Meta:
        abstract = True
