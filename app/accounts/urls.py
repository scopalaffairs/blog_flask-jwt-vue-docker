from django.urls import path

from .views import UserUpdateView
from .views import signup

urlpatterns = [
    path(r'signup/', signup, name='signup'),
    path(r'settings/account/', UserUpdateView.as_view(), name='my_account'),

]
