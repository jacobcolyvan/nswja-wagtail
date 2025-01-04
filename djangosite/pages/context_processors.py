from wagtail.models import Page

from djangosite.pages.models import HomePage


def navigation(request):
    # Get the HomePage instance
    home_page = HomePage.objects.first()

    if home_page:
        # Get immediate children of HomePage that are set to show in menus
        child_pages = (
            Page.objects.child_of(home_page)  # type: ignore[attr-defined]
            .live()
            .in_menu()
            .specific()
            .order_by("path")
        )
        # Combine HomePage with its children
        navigation_pages = [home_page, *list(child_pages)]
    else:
        navigation_pages = []

    return {"navigation_pages": navigation_pages}
