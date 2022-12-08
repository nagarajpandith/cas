from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateStaffForm
from .forms import CreateItemForm
from django.contrib.auth.decorators import user_passes_test
from .models import Account
from .models import Item
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

def addItems(request):
    form = CreateItemForm()

    if request.method=='POST':
        form=CreateItemForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Item added successfully")
            return redirect("addItems")
            
    context = {"form": form}
    return render(request, "editItems.html", context)

def updateItem(request,itemNo):
    item=Item.objects.get(itemNo=itemNo)
    form=CreateItemForm(instance=item)

    if request.method=='POST':
        form=CreateItemForm(request.POST,request.FILES,instance=item)

        if form.is_valid():
            form.save()
        messages.success(request, "Item modified successfully")
        return redirect("items")

            
    context = {"form": form}
    return render(request, "editItems.html", context)

def deleteItem(request,itemNo):
    item=get_object_or_404(Item,itemNo=itemNo)
    messages.success(request, "Item deleted successfully")
    return redirect("items")

def items(request):
    items=Item.objects.all()
    context={'items':items}
    return render(request, "items.html", context)