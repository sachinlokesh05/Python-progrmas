import django
from django.conf.urls import url
from django.views.generic import TemplateView

from pkg_resources import parse_version

from . import views

django_version = parse_version(django.get_version())
if django_version <= parse_version("1.9"):
    from django.conf.urls import patterns

home = TemplateView.as_view(template_name="home.html")

patterns_list = [
    url(
        r"^column_highchart/json/$",
        views.line_chart_json,
        name="column_highchart_json",
    ),
]

if django_version <= parse_version("1.9"):
    urlpatterns = patterns("", *patterns_list)
else:
    urlpatterns = patterns_list
