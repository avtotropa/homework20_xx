from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import CoursesView, CourseDetailView, ContactsView, CourseCreateView, VersionListView, \
    CourseDeleteView, CourseUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', CoursesView.as_view(), name='courses'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('course_descrip/<int:pk>/', CourseDetailView.as_view(), name='courses_descrip'),
    path('create/', CourseCreateView.as_view(), name='create_course'),
    path('delete/<int:pk>/', CourseDeleteView.as_view(), name='delete_course'),
    path('update/<int:pk>/', CourseUpdateView.as_view(), name='update_course')
    # path('course_descrip/<int:pk>/', VersionListView.as_view(), name='version_detail')
]
