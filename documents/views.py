from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from weasyprint import HTML
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView, FormView
from .forms import InvoiceForm


class DocumentsPageView(LoginRequiredMixin, TemplateView):
    template_name = 'documents/documents.html'


class InvoiceFormView(LoginRequiredMixin, FormView):
    template_name = 'documents/invoce_create.html'
    form_class = InvoiceForm
    success_url = '/'

    def form_valid(self, form):
        invoice_number = form.cleaned_data['invoice_number']
        seller_company_name = form.cleaned_data['seller_company_name']
        data = {
            'invoice_number': invoice_number,
            'date': form.cleaned_data['date'],
            'seller_company_name': seller_company_name,
            'address': form.cleaned_data['address'],
            'inn_kpp_seller': form.cleaned_data['inn_kpp_seller'],
            'shipper_address': form.cleaned_data['shipper_address']
        }
        html_string = render_to_string('documents/invoice_template.html', data)
        html = HTML(string=html_string)
        html.write_pdf(target='/tmp/{}_{}.pdf'.format(invoice_number, seller_company_name))
        fs = FileSystemStorage('/tmp')
        with fs.open('{}_{}.pdf'.format(invoice_number, seller_company_name)) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="{}_{}.pdf"'.format(invoice_number,
                                                                                        seller_company_name)
            return response
        return super().form_valid(form)


@login_required
def html_to_pdf_view(request):
    html_string = render_to_string('documents/waybill_template.html')

    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/mypdf.pdf')

    fs = FileSystemStorage('/tmp')
    with fs.open('mypdf.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
        return response

    return response


@login_required
def pdf_template_view(request):
    return render(request, template_name='documents/waybill_template.html')
