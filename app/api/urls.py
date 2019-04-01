from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from .views import CreateView, DetailsView, UserView, UserDetailsView

urlpatterns = [

    # JWT
    path(r'auth/obtain_token/', obtain_jwt_token),
    path(r'auth/refresh_token/', refresh_jwt_token),
    path(r'auth/verify_token/', verify_jwt_token),

    path(r'auth', include('rest_framework.urls',
                          namespace='rest_framework')),

    path(r'bucketlists', CreateView.as_view(), name='create'),
    path(r'bucketlists/<int:pk>',
         DetailsView.as_view(), name="details"),

    path(r'users', UserView.as_view(), name="users"),
    path(r'users/<int:pk>',
         UserDetailsView.as_view(), name="user_details"),
    path(r'get-token/', obtain_auth_token),

]

urlpatterns = format_suffix_patterns(urlpatterns)
