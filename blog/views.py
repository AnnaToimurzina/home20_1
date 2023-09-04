from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from blog.models import Blog



class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        context['title'] = 'Blog'
        return context

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogCreateView(CreateView):
    template_name = 'blog/blog_form.html'
    model = Blog
    fields = ['title', 'content', 'image', 'is_published']
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_form = form.save()
            new_form.slug = slugify(new_form.title)
            new_form.save()

            return super().form_valid(form)

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset=queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'content', 'image', 'is_published']

    def form_valid(self, form):
        if form.is_valid():
            new_form = form.save()
            new_form.slug = slugify(new_form.title)
            new_form.save()

            return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')

    def toggle_activity(request, pk):
        material = get_object_or_404(Blog, pk=pk)
        if material.is_published:
            material.is_published = False
        else:
            material.is_published = True

        material.save()

        return redirect(reverse('blog:list'))