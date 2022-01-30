from django.urls import re_path
from django.contrib import admin
from django.core.exceptions import ImproperlyConfigured

from cities.util import patterns


app_name = "test_app"

urlpatterns = patterns(
    '',
    # Examples:
    # re_path(r'^$', 'test_project.views.home', name='home'),
    # re_path(r'^blog/', include('blog.urls')),

    re_path(r'^admin/', admin.site.urls),
)
