from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from quiz_project.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from random import randrange


def user_signup(request):
    if request.method == "POST":
        un = request.POST.get("un")
        try:
            usr = User.objects.get(username=un)
            return render(request, "login/user_signup.html", {"msg": "Email already registered"})
        except User.DoesNotExist:
            pw = ""
            text = "abcdefghijklmnopqrstuvwxyz123456789"
            for i in range(5):
                pw = pw + text[randrange(len(text))]
            print(pw)

            sub = "Quizz App"
            msg = "Your Password is " + str(pw)
            sender = EMAIL_HOST_USER
            receiver = [str(un)]
            send_mail(sub, msg, sender, receiver)

            usr = User.objects.create_user(username=un, password=pw)
            usr.save()
            return redirect("user_login")
    else:
        return render(request, "login/user_signup.html")


def user_login(request):
    if request.method == "POST":
        un = request.POST.get("un")
        pw = request.POST.get("pw")
        usr = authenticate(username=un, password=pw)
        if usr is None:
            return render(request, "login/user_login.html", {"msg": "Check Credentials"})
        else:
            login(request, usr)
            return redirect("home")
    else:
        return render(request, "login/user_login.html")


def user_logout(request):
    logout(request)
    return redirect("user_login")


def user_np(request):
    if request.method == "POST":
        un = request.POST.get("un")
        try:
            usr = User.objects.get(username=un)

            pw = ""
            text = "abcdefghijklmnopqrstuvwxyz123456789"
            for i in range(5):
                pw = pw + text[randrange(len(text))]
            print(pw)

            sub = "Quizz App"
            msg = "Your New Password is " + str(pw)
            sender = EMAIL_HOST_USER
            receiver = [str(un)]
            send_mail(sub, msg, sender, receiver)

            usr.set_password(pw)
            usr.save()
            return redirect("user_login")

        except User.DoesNotExist:
            return render(request, "login/user_np.html", {"msg": "Email not registered"})
    else:
        return render(request, "login/user_np.html")


def about_me(request):
    return render(request, "login/about_me.html")
