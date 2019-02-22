from django.urls import path
from .views import DocumentsPageView, InvoiceCreateView

app_name = 'documents'
urlpatterns = [
    path('', DocumentsPageView.as_view(), name='documents'),
    path('create-invoice', InvoiceCreateView.as_view(), name='create_invoice'),
]
