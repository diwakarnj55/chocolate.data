from django.shortcuts import render, redirect
from . models import Product
from . forms import ContactForm

def index(request):
    pro=Product.objects.all()
    con=ContactForm
    data ={
        "pro":pro,
        "con":con,
    }
    if request.method=="POST":
        Contact=ContactForm(request.POST)
        if Contact.is_valid():
            Contact.save()
            return redirect("home")
    return render(request,"index.html",data)
