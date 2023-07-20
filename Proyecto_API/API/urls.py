from django.urls import path
from .views import CompanyView
urlpatterns = [
    path('companies/',CompanyView.as_view(), name='companies_list'),
    path('companies/<int:id>',CompanyView.as_view(), name='companies_process'), #Esto hace que podamos listar de una a una las compañias mediante el id
]

