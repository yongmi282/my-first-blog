from django.conf.urls import url, include #is include the error?
from . import views
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
