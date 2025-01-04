from typing import ClassVar

from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.contrib.settings.models import BaseGenericSetting, register_setting


@register_setting
class ContactSettings(BaseGenericSetting):
    position = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)

    panels: ClassVar[list] = [
        FieldPanel("name"),
        FieldPanel("position"),
        FieldPanel("email"),
        FieldPanel("mobile"),
    ]

    class Meta:
        verbose_name = "Contact Settings"
