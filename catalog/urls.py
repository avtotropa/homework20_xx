from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import CoursesView, CourseDetailView, ContactsView, CourseCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', CoursesView.as_view(), name='courses'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('course_descrip/<int:pk>/', CourseDetailView.as_view(), name='courses_descrip'),
    path('create/', CourseCreateView.as_view(), name='create_course')
]
