from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def view_all(request):
    return HttpResponse('Ми на першій сторінці')


def view_spacial_case_2020(request):
    return HttpResponse('Ми на спеціальному 2020 році')


def view_year(request, year):
    return HttpResponse(f'Ми на {year} році')


def view_year_month(request, year, month):
    return HttpResponse(f'Ми на {year} році та {month} місяці')
