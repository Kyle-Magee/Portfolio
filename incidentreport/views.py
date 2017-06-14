from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Report
from .form import ReportForm

def homepage(request):
    context = {
        'form': ReportForm,
        'reports': Report.objects.all()

    }
    if request.method == 'POST':
        print(context['reports'])
        form = ReportForm(request.POST)
        if form.is_valid():
            report = Report(user=form['user'].data,
                            device=form['device'].data,
                            location=form['location'].data,
                            date=form['date'].data, 
                            time=form['time'].data)
            report.save()
            return redirect(reverse(homepage))
    return render(request, 'ir.html', context)