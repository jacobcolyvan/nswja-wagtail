from typing import ClassVar

from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page

from djangosite.pages.blocks import (
    CTACardBlock,
)

from .mixins import HeroMixin


class HomePage(Page, HeroMixin):
    template = "pages/home_page.html"
    parent_page_types: ClassVar = ["wagtailcore.Page"]

    main_content = RichTextField(blank=True)
    cta_cards = StreamField(
        [("cta_card", CTACardBlock())],
        use_json_field=True,
        blank=True,
    )

    content_panels: ClassVar[list] = [
        *Page.content_panels,
        *HeroMixin.hero_panels,
        FieldPanel("main_content"),
        FieldPanel("cta_cards"),
    ]
