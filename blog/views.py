from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic
from taggit.models import Tag
from django.contrib import messages
from .forms import CommentForm, PostForm
from .models import Post, Comment


# Create your views here.

class PostList(generic.ListView):
    paginate_by = 5
    model = Post
    template_name = 'blog/post/list.html'

    def get_queryset(self):
        order_by = self.request.GET.get('sort')
        context = Post.objects.filter(status=1).order_by('created_date') \
            if order_by == "1" else Post.objects.filter(status=1).order_by('-created_date')

        return context

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['sort'] = self.request.GET.get('sort')
        return context


class PostView(generic.DetailView):
    model = Post
    template_name = 'blog/post/detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context['tags'] = self.object.tags.all()
        return context


class DeletePostView(generic.DeleteView):
    model = Post

    def get_success_url(self):
        messages.success(self.request, 'Usunięto element!')
        return reverse_lazy('home')


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        post.delete()
        return JsonResponse({'data': True})

    return JsonResponse({'data': False})


class AddPostView(generic.CreateView):
    model = Post
    template_name = 'blog/post/add_post.html'
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post-details', kwargs={'pk': self.object.pk})


class AddCommentView(generic.CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/post/add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post-details', kwargs={'pk': self.object.post.pk})


class PostByTag(generic.ListView):
    template_name = 'blog/post/list.html'

    def get_queryset(self):
        order_by = self.request.GET.get('sort')
        context = Post.objects.filter(tags=get_object_or_404(Tag, name=self.kwargs['slug'])).order_by('created_date') \
            if order_by == "1" else Post.objects.filter(tags=get_object_or_404(Tag, name=self.kwargs['slug'])).order_by(
            '-created_date')
        return context

    def get_context_data(self, **kwargs):
        context = super(PostByTag, self).get_context_data(**kwargs)
        context['sort'] = self.request.GET.get('sort')
        return context


class TagList(generic.ListView):
    template_name = 'blog/tag/list.html'

    def get_queryset(self):
        return Tag.objects.all()


def error_404(request, exception):
    return render(request, '404.html')
