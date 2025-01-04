from wagtail.models import Page


def navigation(request):
    # TODO: fix this
    # root_page = request.site.root_page
    root_page = Page.objects.get(id=1)

    # Get all immediate children of the root that are set to show in menus
    navigation_pages = (
        Page.objects.child_of(root_page)  # type: ignore[attr-defined]
        .live()
        .in_menu()
        .specific()
        .order_by("path")
    )

    return {"navigation_pages": navigation_pages}
