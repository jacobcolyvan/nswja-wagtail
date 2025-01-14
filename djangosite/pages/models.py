from typing import ClassVar

from django.db.models import BooleanField, CharField, IntegerField
from django.utils.translation import gettext_lazy
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page

from djangosite.pages.blocks import (
    AccordionItemBlock,
    BoardMemberBlock,
    CoreTeamBlock,
    CTACardBlock,
    FormBlock,
)
from djangosite.pages.mixins import HeroMixin


class BasePage(Page):
    default_show_in_menus = True
    menu_sort_order = IntegerField(default=0)

    subtitle = CharField(max_length=255, blank=True)
    include_contact_details = BooleanField(
        default=False,
        help_text="Include contact details at the bottom of the page.",
    )
    main_content = RichTextField(blank=True)

    content_panels: ClassVar[list] = [
        *Page.content_panels,
        FieldPanel("subtitle"),
        FieldPanel("include_contact_details"),
        FieldPanel("main_content"),
    ]
    # Same as Page.promote_panels, but with menu_sort_order added
    promote_panels: ClassVar[list] = [
        MultiFieldPanel(
            [
                FieldPanel("slug"),
                FieldPanel("seo_title"),
                FieldPanel("search_description"),
            ],
            gettext_lazy("For search engines"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("show_in_menus"),
                FieldPanel("menu_sort_order"),
            ],
            gettext_lazy("For site menus"),
        ),
    ]

    class Meta:
        abstract = True


class HomePage(BasePage, HeroMixin):
    template = "pages/home_page.html"
    parent_page_types: ClassVar[list] = ["wagtailcore.Page"]
    max_count = 1

    cta_cards = StreamField(
        [("cta_card", CTACardBlock())],
        use_json_field=True,
        blank=True,
    )

    content_panels: ClassVar[list] = [
        *Page.content_panels,
        *HeroMixin.content_panels,
        FieldPanel("include_contact_details"),
        FieldPanel("main_content"),
        FieldPanel("cta_cards"),
    ]
    # Same as BasePage.promote_panels, but without menu options
    promote_panels: ClassVar[list] = [
        MultiFieldPanel(
            [
                FieldPanel("slug"),
                FieldPanel("seo_title"),
                FieldPanel("search_description"),
            ],
            gettext_lazy("For search engines"),
        )
    ]


class GeneralPage(BasePage):
    template = "pages/general_page.html"
    parent_page_types: ClassVar[list] = ["pages.HomePage"]
    subpage_types: ClassVar[list] = ["pages.GeneralPage"]

    cta_cards = StreamField(
        [("cta_card", CTACardBlock())],
        use_json_field=True,
        blank=True,
        help_text="These are good for adding links to other pages on the site.",
    )

    accordions = StreamField(
        [("accordion_item", AccordionItemBlock())],
        help_text=(
            "These are good for adding collapsible content to the page, like "
            "FAQs or other content that can be grouped together."
        ),
        use_json_field=True,
        blank=True,
    )

    content_panels: ClassVar[list] = [
        *BasePage.content_panels,
        FieldPanel("accordions"),
    ]


class AboutPage(BasePage):
    template = "pages/about_page.html"
    parent_page_types: ClassVar[list] = ["pages.HomePage"]
    subpage_types: ClassVar[list] = []
    max_count = 1

    core_team = StreamField(
        [("core_team_member", CoreTeamBlock())],
        use_json_field=True,
        blank=True,
    )
    board_members = StreamField(
        [("board_member", BoardMemberBlock())],
        use_json_field=True,
        blank=True,
    )

    content_panels: ClassVar[list] = [
        *BasePage.content_panels,
        FieldPanel("core_team"),
        FieldPanel("board_members"),
    ]


class FormsPage(BasePage):
    template = "pages/forms_page.html"
    parent_page_types: ClassVar[list] = ["pages.HomePage"]
    subpage_types: ClassVar[list] = []
    max_count = 1

    forms = StreamField(
        [("form", FormBlock())],
        use_json_field=True,
        blank=True,
    )

    content_panels: ClassVar[list] = [
        *BasePage.content_panels,
        FieldPanel("forms"),
    ]
