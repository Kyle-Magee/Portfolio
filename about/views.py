from django.shortcuts import render
from .models import UserInformation, Roles

# Create your views here.


def view_about(request):
    user_info = UserInformation.objects.all()[0]
    roles = Roles.objects.order_by('relevance')
    context = {
        'user_info': user_info,
        'roles': roles,
    }
    return render(request, 'about.html', context)