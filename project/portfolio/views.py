from django.shortcuts import render, redirect
from django.contrib import messages
from portfolio.models import Contact, Blogs

# Create your views here.
def home(request):
    return render(request, 'home.html')

def handleblog(request):
    posts= Blogs.objects.all()
    context= {"posts":posts}
    return render(request, 'handleblog.html', context)


def about(request):
    return render(request, 'about.html')

def contact(request):

    if request.method=="POST":
        fname= request.POST.get('name')
        femail= request.POST.get('email')
        fphoneno= request.POST.get('num')
        fdesc= request.POST.get('desc')
        
        query= Contact(name= fname, email=fname, phonenumber=fphoneno, description= fdesc)
        query.save()
        messages.success(request, "Thank you for reaching out. I will get back to you soon.")
        return redirect("/contact")


    return render(request, 'contact.html')

  