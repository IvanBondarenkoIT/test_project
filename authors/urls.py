from django.urls import path
from .views import *

urlpatterns = [
    path('', view_all_authors),
    path('<int:year>/', view_year_authors),
]