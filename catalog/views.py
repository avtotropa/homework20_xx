from django.shortcuts import render

from catalog.models import Course


def courses(request):
    context = {
        'object_list': Course.objects.all(),
        'base_title': 'Sky.pro',
        'title': 'Учим IT-профессиям с нуля и гарантируем новую работу.'
    }
    return render(request, 'catalog/courses.html', context)


def contacts(request):
    return render(request, 'catalog/contacts.html')


def courses_descrip(request, course_id):
    course = Course.objects.get(pk=course_id)
    return render(request, 'catalog/courses_descrip.html', {'course': course})
