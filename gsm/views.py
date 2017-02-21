from django.shortcuts import render
from gsm2.build_output import build_output
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import FormView
from django.core.files.storage import FileSystemStorage
from .form import TemplateForm
from django.core.files.base import ContentFile
from django.views.static import serve
from gsm2 import build_output
import os


# Create your views here.
def handle(f):
    with open('media/doc.xlsx', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def Homepage(request):
    if request.method == 'POST':
        form = TemplateForm(request.POST, request.FILES)
        handle(request.FILES['template_file'])
        build_output.build_output(filename='doc.xlsx', template_file='doc.xlsx', startdate='09/10/17', folder='media')
        return serve(request, document_root='', path='002.xlsx')
    else:
        form = TemplateForm()
    return render(request, 'gsm.html', {'form': form})
"""
class Homepage(FormView):
    form_class = TemplateForm
    template_name = 'gsm.html'

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        template_file = ContentFile(request.FILES['template'])
        template_file.save('test.doc')
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        template_file = ContentFile(request.FILES['template'])
        template_file.save('test.doc')

        return 'thanks'
"""
