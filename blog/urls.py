from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('post/<int:pk>', views.PostView.as_view(), name='post-details'),
    path('post/<slug:slug>', views.PostView.as_view(), name='post-details'),
    path('post/<int:pk>/delete', views.post_delete, name='post-delete'),
    path('tag', views.TagList.as_view()),
    path('tag/<slug:slug>', views.PostByTag.as_view())
]