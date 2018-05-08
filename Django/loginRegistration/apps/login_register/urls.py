from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register/process$', views.reg_process),
    url(r'^login/process$', views.log_process),
    url(r'^success$', views.success),
    url(r'^logout$', views.logout)
]