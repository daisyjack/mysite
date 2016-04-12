from django.conf.urls import patterns, include, url
from django.contrib import admin
from hello.views import *
from contact.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r"^hello/$", hello),
    (r'^time/$', current_datetime),
    url(r"^time/plus/(\d{1,2})/$", hours_ahead),
    url(r"^search/$", search),
    url(r"^contact/$", contact),
    url(r"^image/$", unruly_passengers_csv),
    url(r"^json/$", json_type),
    url(r'^admin/', include(admin.site.urls)),
)
