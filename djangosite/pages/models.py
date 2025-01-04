from typing import ClassVar

from django.db.models import BooleanField
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page

from djangosite.pages.blocks import CTACardBlock
from djangosite.pages.mixins import HeroMixin


class BasePage(Page):
    include_contact_details = BooleanField(
        default=False,
        help_text="Include contact details at the bottom of the page.",
    )

    class Meta:
        abstract = True


class HomePage(BasePage, HeroMixin):
    template = "pages/home_page.html"
    parent_page_types: ClassVar[list] = ["wagtailcore.Page"]

    main_content = RichTextField(blank=True)
    cta_cards = StreamField(
        [("cta_card", CTACardBlock())],
        use_json_field=True,
        blank=True,
    )

    content_panels: ClassVar[list] = [
        *Page.content_panels,
        FieldPanel("include_contact_details"),
        *HeroMixin.hero_panels,
        FieldPanel("main_content"),
        FieldPanel("cta_cards"),
    ]
