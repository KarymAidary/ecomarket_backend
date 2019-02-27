from django.urls import path
from .views import *

app_name = 'stock'
urlpatterns = [
    path('pdf_view', pdf_view, name='pdf_view'),
    path('write_pdf_view', write_pdf_view, name='write_pdf_view'),

]
