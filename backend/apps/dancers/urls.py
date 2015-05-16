from django.conf.urls import patterns, url
from views import *


urlpatterns = patterns('',
    url(r'^parents-list/$', ParentListView.as_view(), name="dancer-list"),
    url(r'^student-intake-form/$', StudentIntakeFormListView.as_view(), name="dancer-list"),
)

