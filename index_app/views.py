from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def index(request):
    # getting data from database
    coffees = Coffee.objects.all()
    list1 = []
    list2 = []
    count = 0
    for i in coffees:
        if count % 2 == 0:
            list1.append(i)
        else:
            list2.append(i)
        count += 1

    # getting data 
    name = request.GET.get("name")
    email = request.GET.get("email")
    text = request.GET.get("message")
    if name is not None and email is not None and text is not None:
        ClientComment.objects.create(name=name, email=email, text=text)
        return redirect("/")
    return render(request, "index_app/index.html", context={"list1": list1, "list2": list2})
