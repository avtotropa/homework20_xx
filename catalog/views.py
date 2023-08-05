from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView, ListView, DeleteView, UpdateView

from catalog.forms import CourseForm, VersionForm
from catalog.models import Course, Version


class CoursesView(TemplateView):
    template_name = 'catalog/courses.html'
    extra_context = {
        'base_title': 'Skypro',
        'title': 'Учим IT-профессиям с нуля и гарантируем новую работу.'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Course.objects.all()

        return context_data


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'


class CourseDetailView(LoginRequiredMixin, DetailView):
    model = Course

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        course = self.get_object()
        context_data['object_list'] = Version.objects.filter(course=course, is_active=True)

        return context_data


class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    form_class = CourseForm
    success_url = reverse_lazy('catalog:courses')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Course, Version, form=VersionForm, extra=1)
        context_data['formset'] = VersionFormset()

        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST)
        else:
            context_data['formset'] = VersionFormset()

        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        form.instance.author = self.request.user

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class VersionListView(ListView):
    model = Version


class CourseDeleteView(LoginRequiredMixin, DeleteView):
    model = Course
    success_url = reverse_lazy('catalog:courses')


class CourseUpdateView(LoginRequiredMixin, UpdateView):
    model = Course
    form_class = CourseForm
    success_url = reverse_lazy('catalog:courses')

    def get_context_data(self, **kwargs):

        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Course, Version, form=VersionForm, extra=1)
        context_data['formset'] = VersionFormset()

        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)

        return context_data

    def form_valid(self, form):

        formset = self.get_context_data()['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
            
        return super().form_valid(form)
