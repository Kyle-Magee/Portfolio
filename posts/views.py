from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.


def post_list(request):
    query_set = Post.objects.order_by('created_date').reverse()
    context = {
        'posts': query_set

    }
    return render(request, "post_list.html", context)


def post_page(request, id):
    instance = get_object_or_404(Post, id=id)
    context = {
        "post": instance
    }
    return render(request, "post_page.html", context)
