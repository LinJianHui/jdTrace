from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from shop.models import UserInterest, Product
# Create your views here.


def signUp(request):
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return render(request, "registration/login.html")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


@login_required()
def interstList(request):
    user = request.user
    interests = UserInterest.objects.filter(user=user)
    return render(request, "usercenter/myinterest.html",
                  {'interests': interests})


@login_required()
def addinterst(request, productId):
    user = request.user
    if UserInterest.objects.filter(user=user,
                                   product_id=productId).count() == 0:
        userInterest = UserInterest()
        userInterest.user = user
        userInterest.product = Product.objects.get(pk=productId)
        userInterest.save()
    return redirect('usercenter:myinterests')


@login_required()
def removeinterst(request, productId):
    user = request.user
    UserInterest.objects.filter(user=user,
                                product_id=productId).delete()
    return redirect('usercenter:myinterests')

