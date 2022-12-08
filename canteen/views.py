from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateStaffForm
from django.contrib.auth.decorators import user_passes_test
from .models import *
from django.contrib.auth.models import User
import uuid

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


def order(request):
    items = Item.objects.all()
    context = {"items": items}

    if request.method == "POST":
        item_ids = request.POST.getlist("item_ids")
        quantities = request.POST.getlist("quantities")

        # Create the order object and save it
        token = int(str(uuid.uuid4().int)[:3])
        print(token)
        order = Order(tokenNo=token)
        order.save()

        # Create the order items and add them to the order
        for item_id, quantity in zip(item_ids, quantities):
            item = Item.objects.get(itemNo=item_id)

            # Get the queryset of order items with the same item
            order_items = OrderItem.objects.filter(item=item)

            # Update the quantity of the existing order item, or create a new one
            order_item, created = order_items.update_or_create(
                defaults={"quantity": quantity}, item=item
            )

            # Add the order item to the order
            order.items.add(order_item)

        # Calculate and set the total amount for the order
        order.totalAmount = order.get_total()
        order.save()

    return render(request, "order.html", context)
