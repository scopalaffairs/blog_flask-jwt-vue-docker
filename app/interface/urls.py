from django.urls import path

from . import views

urlpatterns = [
    path(r'interface', views.index, name='index'),

    # Test api
    path(r'api/test', views.test_api, name='test_api'),
]

