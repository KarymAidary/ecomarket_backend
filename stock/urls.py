from django.urls import path
from .views import *

app_name = 'stock'
urlpatterns = [
    path('pdf_view', pdf_view, name='pdf_view'),
    path('write_pdf_view', write_pdf_view, name='write_pdf_view'),
    path('html_to_pdf_view', html_to_pdf_view, name='html_to_pdf_view'),
    path('pdf_template_view', pdf_template_view, name='pdf_template_view'),
]
