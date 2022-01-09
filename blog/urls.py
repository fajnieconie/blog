from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post/<int:pk>', views.PostView.as_view(), name='post-details'),
    path('post/<slug:slug>', views.PostView.as_view(), name='post-details'),
    path('post/<int:pk>/delete', login_required(views.DeletePostView.as_view()), name='post-delete'),
    path('post/add/', login_required(views.AddPostView.as_view()), name='add_post'),
    path('post/<int:pk>/comment/', login_required(views.AddCommentView.as_view()), name="add_comment"),
    path('tag/', views.TagList.as_view(), name='tag-list'),
    path('tag/<slug:slug>', views.PostByTag.as_view())
]