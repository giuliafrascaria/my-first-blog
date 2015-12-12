from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})



"""
abbiamo creato un metodo (def) chiamato post_list 
che prende request e restituisce un metodo render 
che ci fornirà (metterà insieme) il nostro template 
blog/post_list.html
"""