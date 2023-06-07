from urllib import request
from django.shortcuts import render, redirect
from .models import Category, Post, Journal, Volume
from django.views import generic
# Create your views here.

def home(request):
    categories = Category.objects.all()
    posts = Post.objects.all()

    context = {'categories': categories, 'posts': posts}
    return render(request,'posts/home.html', context)

def viewpost(request, pk):
    post = Post.objects.get(id = pk)
    return render(request,'posts/viewpost.html', {'post':post})

def aboutus(request):
    return render(request,'posts/aboutus.html')

def addpost(request):
    return render(request,'posts/add.html')

def contact(request):
    return render(request,'posts/contact.html')

class journalview(generic.ListView):
    model = Journal
    template_name = 'posts/technology.html'
    context_object_name = 'files'
    paginate_by = 17

    def get_queryset(self):
        request = self.request
        category = request.GET.get('category')
        if category is not None:
            return Journal.objects.filter(title = category )
        return Journal.objects.order_by('-id')