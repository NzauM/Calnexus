from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings


urlpatterns=[
    url(r'^$',views.index,name='home'),
    url(r'^features/$',views.features,name='features'),
]