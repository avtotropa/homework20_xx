from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, courses, courses_descrip

app_name = CatalogConfig.name

urlpatterns = [
    path('', courses, name='courses'),
    path('contacts/', contacts, name='contacts'),
    path('courses_descrip/<int:course_id>/', courses_descrip, name='courses_descrip'),
]
