from django.conf.urls import include, url
from website.views import website_views

website_urls = [
    url(r'^/?$', website_views.home, name="home"),
    url(r'^projects/?$', website_views.projects, name="projects"),
    url(r'^experimental/?$', website_views.experimental, name="experimental")
]