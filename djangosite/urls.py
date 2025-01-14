from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.contrib.sitemaps.views import sitemap
from wagtail.documents import urls as wagtaildocs_urls

urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("sitemap.xml", sitemap),
]

if settings.DEBUG:
    urlpatterns += [
        path("404/", TemplateView.as_view(template_name="404.html")),
        path("500/", TemplateView.as_view(template_name="500.html")),
    ]

urlpatterns += [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(wagtail_urls)),
]
