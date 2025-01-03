from django.db import models

from wagtail.models import Page


class HomePage(Page):
    template = "pages/home_page.html"
    parent_page_types = ["wagtailcore.Page"]


class GeneralPage(Page):
    template = "pages/general_page.html"
    parent_page_types = ["pages.HomePage"]
