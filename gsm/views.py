from django.shortcuts import render
from gsm2.build_output import build_output
from .form import TemplateForm
from django.views.static import serve
from gsm2 import build_output


def save_template_to_disk(f):
    with open('media/doc.xlsx', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def homepage(request):
    if request.method == 'POST':
        save_template_to_disk(request.FILES['template_file'])
        build_output.build_output(filename='doc.xlsx', template_file='doc.xlsx', startdate='09/10/17', folder='media')
        return serve(request, document_root='', path='002.xlsx')
    else:
        form = TemplateForm()
    return render(request, 'gsm.html', {'form': form})


def gsm_help(request):
    return render(request, template_name='gsm_help.html')
