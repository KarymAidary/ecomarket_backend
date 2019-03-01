from django.urls import path
from .views import ProductListView, CategoryListView, CategoryCreateView

app_name = 'stock'
urlpatterns = [
    # path('pdf_view', pdf_view, name='pdf_view'),
    # path('write_pdf_view', write_pdf_view, name='write_pdf_view'),
    path('', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/', ProductListView.as_view(), name='product_list')

]
