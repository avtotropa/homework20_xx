from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView

from catalog.forms import CourseForm
from catalog.models import Course


class CoursesView(TemplateView):
    template_name = 'catalog/courses.html'
    extra_context = {
        'base_title': 'Sky.pro',
        'title': 'Учим IT-профессиям с нуля и гарантируем новую работу.'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Course.objects.all()

        return context_data


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'


class CourseDetailView(DetailView):
    model = Course


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    success_url = reverse_lazy('catalog:courses')
