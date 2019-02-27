from django.urls import path
from .views import DocumentsPageView, InvoiceFormView, pdf_template_view, html_to_pdf_view

app_name = 'documents'
urlpatterns = [
    path('', DocumentsPageView.as_view(), name='documents'),
    path('create-invoice', InvoiceFormView.as_view(), name='create_invoice'),
    path('html_to_pdf_view', html_to_pdf_view, name='html_to_pdf_view'),
    path('pdf_template_view', pdf_template_view, name='pdf_template_view'),
]
