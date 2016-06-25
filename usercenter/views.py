from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
# Create your views here.


def signUp(request):
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return render(request, "registration/login.html")
    else :
    	form = UserCreationForm()
    return render(request, "registration/signup.html",{"form":form})
