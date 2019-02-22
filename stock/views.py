from django.http import HttpResponse, HttpResponseNotFound
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

from django.template.loader import render_to_string

from weasyprint import HTML


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


def html_to_pdf_view(request):
    paragraphs = ['first paragraph', 'second paragraph', 'third paragraph']

    html_string = render_to_string('stock/pdf_template.html', {'paragraphs': paragraphs})

    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/mypdf.pdf')

    fs = FileSystemStorage('/tmp')
    with fs.open('mypdf.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
        return response

    return response


def pdf_template_view(request):
    return render(request, template_name='documents/invoice_template.html')