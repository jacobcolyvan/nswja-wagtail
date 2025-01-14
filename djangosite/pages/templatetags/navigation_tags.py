from django import template
from wagtail.models import Page

from djangosite.pages.models import HomePage

register = template.Library()


def _get_sorted_menu_pages(parent_page):
    """
    Get all menu-enabled child pages of a parent page, sorted by menu order.
    """
    pages = (
        Page.objects.child_of(parent_page)  # type: ignore[attr-defined]
        .live()
        .in_menu()
        .specific()
    )
    return sorted(pages, key=lambda x: (x.menu_sort_order, x.path))


@register.simple_tag()
def get_navigation_pages():
    home_page = HomePage.objects.first()

    if not home_page:
        return {"navigation_pages": {"home_page": None, "items": []}}

    navigation_structure = []
    for child in _get_sorted_menu_pages(home_page):
        child_structure = {"page": child, "children": []}
        for grandchild in _get_sorted_menu_pages(child):
            grandchild_structure = {"page": grandchild, "children": []}
            child_structure["children"].append(grandchild_structure)

        navigation_structure.append(child_structure)

    home_page_dict = {"page": home_page, "children": []}
    return [home_page_dict, *navigation_structure]
