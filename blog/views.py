from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from taggit.models import Tag

from .models import Post


# Create your views here.

class PostList(generic.ListView):
    paginate_by = 5
    model = Post
    queryset = Post.objects.filter(status=1).order_by('published_date')
    template_name = 'blog/post/list.html'


class PostView(generic.DetailView):
    model = Post
    template_name = 'blog/post/detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context['tags'] = self.object.tags.all()
        return context


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        post.delete()
        return JsonResponse({'data': True})

    return JsonResponse({'data': False})


class PostByTag(generic.ListView):
    template_name = 'blog/post/list.html'

    def get_queryset(self):
        return Post.objects.filter(
            tags=get_object_or_404(Tag, name=self.kwargs['slug'])
        )


class TagList(generic.ListView):
    template_name = 'blog/tag/list.html'

    def get_queryset(self):
        return Tag.objects.all()
