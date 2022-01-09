from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post/<int:pk>', views.PostView.as_view(), name='post-details'),
    path('post/<slug:slug>', views.PostView.as_view(), name='post-details'),
    path('post/<int:pk>/delete', views.DeletePostView.as_view(), name='post-delete'),
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
    path('post/<int:pk>/comment/', views.AddCommentView.as_view(), name="add_comment"),
    path('tag/', views.TagList.as_view()),
    path('tag/<slug:slug>', views.PostByTag.as_view())
]