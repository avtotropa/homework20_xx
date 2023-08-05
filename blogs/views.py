from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blogs.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('header', 'content', 'image',)
    success_url = reverse_lazy('blogs:blogs')

    def form_valid(self, form):

        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.header)
            new_blog.save()

        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = context['object_list']

        for blog in queryset:
            blog.short_content = blog.content[:97] + '...' if len(blog.content) > 100 else blog.content

        return context

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_views += 1
        self.object.save()

        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('header', 'content', 'image',)
    success_url = reverse_lazy('blogs:blogs')


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blogs:blogs')
