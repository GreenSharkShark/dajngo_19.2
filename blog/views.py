from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import BlogPost


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/test.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        self.object.slug = slugify(self.object.title)
        return self.object

    def get_success_url(self):
        return reverse('blog:test', args=[self.kwargs.get('pk')])


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/test2.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogPostView(CreateView):
    model = BlogPost
    fields = ('title', 'body', 'preview',)
    success_url = reverse_lazy('blog:test')


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ('title', 'body', 'preview',)
    success_url = reverse_lazy('blog:test')


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blog:test')
