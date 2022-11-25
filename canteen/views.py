from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateStaffForm
from django.contrib.auth.decorators import user_passes_test
from .models import Account
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, "index.html")


def loginView(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        # User Authentication
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.info(request, "Username OR password is incorrect")

        context = {}
        return render(request, "login.html", context)


def logoutUser(request):
    logout(request)
    return redirect("login")


def register(request):
    form = CreateStaffForm()
    if request.method == "POST":
        form = CreateStaffForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            phone = form.cleaned_data.get("phone")
            city = form.cleaned_data.get("city")
            state = form.cleaned_data.get("state")
            pincode = form.cleaned_data.get("pincode")
            Account.objects.create(
                user=User.objects.get(username=user),
                email=email,
                phone=phone,
                city=city,
                state=state,
                pincode=pincode,
                isKStaff="True",
            )
            messages.success(request, user + "was registered as Kitchen Staff")

            return redirect("register")

    context = {"form": form}
    return render(request, "registerStaff.html", context)
