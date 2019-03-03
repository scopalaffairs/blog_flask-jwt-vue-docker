from django.urls import path

from .views import BoardListView
from .views import PostListView
from .views import PostUpdateView
from .views import TopicListView
from .views import new_topic
from .views import reply_topic

urlpatterns = [
    path(r'', BoardListView.as_view(), name='home'),

    path(r'boards/<int:pk>/', TopicListView.as_view(), name='board_topics'),
    path(r'boards/<int:pk>/new/', new_topic, name='new_topic'),
    path(r'boards/<int:pk>/topics/<int:topic_pk>/', PostListView.as_view(), name='topic_posts'),
    path(r'boards/<int:pk>/topics/<int:topic_pk>/reply/', reply_topic, name='reply_topic'),
    path(r'boards/<int:pk>/topics/<int:topic_pk>/posts/<int:post_pk>)/edit/', PostUpdateView.as_view(),
         name='edit_post')
]
