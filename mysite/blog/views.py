from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})



"""
abbiamo creato un metodo (def) chiamato post_list 
che prende request e restituisce un metodo render 
che ci fornirà (metterà insieme) il nostro template 
blog/post_list.html
"""