from django.shortcuts import render,redirect
from home.forms import ProfileForm,infoprofileform
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout,login

from django.contrib.auth.hashers import check_password
# Create your views here.
def index(request):
    return render(request,"index.html")

def profile_reg(request):
    register=False
    if request.method=="POST":
        profile_form=ProfileForm(data=request.POST)
        info_form=infoprofileform(data=request.POST)

        if profile_form.is_valid() and info_form.is_valid():
            user=profile_form.save()
            user.save()
            profile=info_form.save(commit=False)
            profile.user=user
            profile.save()
            register=True
        else:
            HttpResponse("<h2>Something Went Wrong With The Form.</h2>")
    else:
        profile_form = ProfileForm(data=request.POST)
        info_form = infoprofileform(data=request.POST)
    return render(request,'Register.html',{
                            'profile_form':profile_form,
                            'info_form':info_form,
                            'register':register
        })

def loginuser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username)
        p=check_password(password,)
        if user is not None:
            login(request,user)
            return redirect("/index")
        else:
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    return redirect("/login")

