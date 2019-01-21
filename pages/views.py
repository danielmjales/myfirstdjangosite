from django.http import HttpResponse
from django.shortcuts import render
from .forms import PostForm

# Create your views here.

# def home_view(request, *args, **kwargs):
#     #return HttpResponse("<h1>Hello World</h1>")
#     my_context={
#         "my_text": 'this is about us',
#         "my_number": 123
#     }
#     return render(request, "home.html", my_context) 

def index_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello World</h1>")
    return render(request, "pages/index.html", {})

def contact_view(request, *args, **kwargs):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponse("<h1>Thanks! I will be in touch with you soon.</h1>")
    else:
        form = PostForm()
    return render(request, 'pages/contact.html', {'form': form})