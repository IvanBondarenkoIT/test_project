from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def view_all_authors(request):
    return HttpResponse('Ми на першій сторінці про авторів')


def view_year_authors(request, year):
    return HttpResponse(f'Перелік авторів за {year} рік')
