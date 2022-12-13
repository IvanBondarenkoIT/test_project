from django.urls import path
from .views import *

urlpatterns = [
    path('', view_all),
    path('2020/', view_spacial_case_2020),
    path('<int:year>/', view_year),
    path('<int:year>/<int:month>', view_year_month),
]