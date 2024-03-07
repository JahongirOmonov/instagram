from django.urls import path
from .views import UserListApiView, StoryActiveListApiView2, \
    PostExploreListApiView, PostDetailApiView, UserPublicListApiView

urlpatterns = [
    path('users/', UserListApiView.as_view()),
    path('public-users/', UserPublicListApiView.as_view()),
    path('explore/', PostExploreListApiView.as_view()),
    path('post-detail/<int:pk>', PostDetailApiView.as_view()),
    path('active-stories/', StoryActiveListApiView2.as_view()),
]
