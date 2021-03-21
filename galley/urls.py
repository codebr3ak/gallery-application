from django.config.urls import url
from . import views
from django.conf import settings

urlpatterns = [
    url(r'^$', views.welcome, name='welcome')
]