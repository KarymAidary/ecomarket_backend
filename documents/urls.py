from django.urls import path
from .views import DocumentsPageView, InvoiceCreateView, pdf_template_view

app_name = 'documents'
urlpatterns = [
    path('', DocumentsPageView.as_view(), name='documents'),
    path('create-invoice', InvoiceCreateView.as_view(), name='create_invoice'),
    path('pdf_template_view', pdf_template_view, name='pdf_template_view'),
]
