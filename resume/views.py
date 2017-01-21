from django.shortcuts import render
from .models import Education, Job

# Create your views here.


def view_resume(request):
    job = Job.objects.all()
    education = Education.objects.all()[0]
    context = {
        'education': education,
        'job': job
    }
    return render(request, 'resume.html', context)