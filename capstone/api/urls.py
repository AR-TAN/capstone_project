from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
    path(
        'v1/adopt/<int:pk>/',
        views.get_delete_update_adopt,
        name='get_delete_update_adopt'
    ),
    path(
        'v1/adopt/',
        views.get_post_adopt,
        name='get_post_adopt'
    ),
    path(
        'v1/users/',
        views.get_users,
        name='get_users'
    ),
    path('v1/users/<int:pk>/',
        views.get_users_detail,
        name='get_users_detail'
    ),
]
