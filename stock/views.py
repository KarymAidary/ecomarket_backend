from django.http import HttpResponse, HttpResponseNotFound
from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_list_or_404
from django.views.generic import CreateView, ListView

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from .models import Product, Category


def pdf_view(request):
    fs = FileSystemStorage()
    filename = 'mypdf.pdf'
    if fs.exists(filename):
        with fs.open(filename) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="mypdf.pdf"'
            return response
    else:
        return HttpResponseNotFound('The requested pdf was not found in our server.')


def write_pdf_view(request):
    doc = SimpleDocTemplate("/tmp/somefilename.pdf")
    styles = getSampleStyleSheet()
    Story = [Spacer(1, 2 * inch)]
    style = styles["Normal"]
    for i in range(100):
        bogustext = ("This is Paragraph number %s.  " % i) * 20
        p = Paragraph(bogustext, style)

        Story.append(p)
        Story.append(Spacer(1, 0.2 * inch))
    doc.build(Story)
    fs = FileSystemStorage("/tmp")
    with fs.open("somefilename.pdf") as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
        return response

    return response


class CategoryListView(ListView):
    template_name = 'stock/list_categories.html'
    model = Category

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['product_list'] = Product.objects.all().order_by('-created_date')
        return context


class CategoryCreateView(CreateView):
    template_name = 'stock/create_category.html'
    model = Category
    fields = ['name', ]
    success_url = '/stock/'


class ProductListView(ListView):
    template_name = 'stock/list_products.html'
    model = Product

    def get_queryset(self):
        queryset = get_list_or_404(
            Product.objects.filter(category__pk=self.kwargs.get("pk")))
        return queryset


class ProductCreateView(CreateView):
    template_name = 'stock/create_product.html'
    model = Product
    fields = ['category', 'vendor_code', 'name', 'amount', 'price', 'trade_price']
    success_url = '/stock/'
