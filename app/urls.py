from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.func, name='ww'),
    url(r'^doPost/$',views.test,name='post')
]