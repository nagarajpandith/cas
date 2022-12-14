from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateStaffForm
from .forms import CreateItemForm
from django.contrib.auth.decorators import user_passes_test
from .models import *
from django.contrib.auth.models import User
import uuid
from django.db.models import Sum
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.hashers import check_password
from reportlab.pdfgen import canvas

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
    if not request.user.is_authenticated:
        return redirect("login")
    form = CreateItemForm()

    if request.method == "POST":
        form = CreateItemForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Item added successfully")
            return redirect("addItems")

    context = {"form": form}
    return render(request, "editItems.html", context)


def updateItem(request, itemNo):
    if not request.user.is_authenticated:
        return redirect("login")

    item = Item.objects.get(itemNo=itemNo)
    form = CreateItemForm(instance=item)

    if request.method == "POST":
        form = CreateItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()
        messages.success(request, "Item modified successfully")
        return redirect("items")

    context = {"form": form}
    return render(request, "editItems.html", context)


def deleteItem(request, itemNo):
    if not request.user.is_authenticated:
        return redirect("login")

    item = get_object_or_404(Item, itemNo=itemNo)
    item.delete()
    messages.success(request, "Item deleted successfully")
    return redirect("items")


def items(request):
    if not request.user.is_authenticated:
        return redirect("login")

    items = Item.objects.all()
    context = {"items": items}
    return render(request, "items.html", context)


def order(request):
    items = Item.objects.all()
    context = {"items": items}

    if request.method == "POST":
        item_ids = request.POST.getlist("item_ids")
        quantities = request.POST.getlist("quantities")
        quantities=[q for q in quantities if q!='0']

        # Generate a new token and check if it is already in use
        token = int(str(uuid.uuid4().int)[:3])
        while Order.objects.filter(tokenNo=token).exists():
            token = int(str(uuid.uuid4().int)[:3])
        order = Order(tokenNo=token)
        order.save()

        # Create the order items and add them to the order
        for item_id, quantity in zip(item_ids, quantities):
            item = Item.objects.get(itemNo=item_id)


            # Update the quantity of the existing order item, or create a new one
            order_item =OrderItem(quantity=quantity,item=item)
            order_item.save()

            # Add the order item to the order
            order.items.add(order_item)

        # Calculate and set the total amount for the order
        order.totalAmount = order.get_total()
        order.save()
        return HttpResponseRedirect("/billing/{}".format(token))

    return render(request, "order.html", context)


def viewOrders(request):
    if not request.user.is_authenticated:
        return redirect("login")

    orders = Order.objects.all()
    context = {"orders": orders}
    return render(request, "viewOrders.html", context)


def markCompleted(request):
    # Get the list of order ids from the request
    order_ids = request.POST.getlist("order_ids")

    # Iterate over the order ids
    for order_id in order_ids:
        # Get the Order object with the specified id
        order = Order.objects.get(tokenNo=order_id)
        # Get the Account instance that corresponds to the current user
        account = Account.objects.get(user=request.user)
        # Update the isCompleted field of the Order object
        Order.objects.filter(tokenNo=order_id).update(
            isCompleted=True, completedBy=account
        )

    # Redirect to the orders page
    return redirect("viewOrders")


def billing(request, tokenNo):
    if not request.user.is_authenticated:
        return redirect("login")

    # Create a queryset with only the specified Order object
    orders = Order.objects.filter(tokenNo=tokenNo)
    modeOfPayment = ""
    if request.method == "POST":
        modeOfPayment = request.POST.get("modeOfPayment")
        password = request.POST.get("password")

        # Check if the entered password is correct
        if check_password(password, request.user.password):
            order = orders.first()
            order.modeOfPayment = modeOfPayment
            order.isPaid = True
            order.save()

            # Generate a bill for the order
            bill = Bill.objects.create(amount=order.totalAmount, order=order)

            bill.save()
            # Create a canvas and set the font size
            c = canvas.Canvas("invoice.pdf")
            c.setFontSize(24)

            # Write the invoice header
            c.drawString(100, 750, "Invoice" + str(order.tokenNo))

            # Set the font size for the table
            c.setFontSize(14)

            # Write the table headers
            c.drawString(100, 725, "Item")
            c.drawString(250, 725, "Quantity")
            c.drawString(350, 725, "Total Amount")

            # Set the font size for the table rows
            c.setFontSize(12)

            # Write the table rows
            y = 700
            for order_item in order.items.all():
                c.drawString(100, y, order_item.item.name)
                c.drawString(250, y, str(order_item.quantity))
                y -= 25

            # Write the total amount
            c.drawString(100, y, "Total Amount")
            c.drawString(350, y, str(order.totalAmount))

            # Write the mode of payment
            c.drawString(100, y - 25, "Mode of Payment")
            c.drawString(350, y - 25, order.get_modeOfPayment_display())

            # Save the PDF
            c.save()

            # Read the generated PDF and send it as response
            with open("invoice.pdf", "rb") as pdf:
                response = HttpResponse(pdf.read(), content_type="application/pdf")
                response["Content-Disposition"] = "attachment; filename=invoice.pdf"
                return response
        else:
            messages.error(request, "Incorrect password")
            return redirect("billing", tokenNo=tokenNo)

    context = {"orders": orders}
    return render(request, "billing.html", context)

def summary(request):

    if not request.user.is_authenticated:
        return redirect("login")

    items_sorted=OrderItem.objects.select_related('item').values('item','item__name').all().annotate(sum=Sum('quantity')).order_by('-sum')
    amount=Order.objects.filter(isPaid=True).aggregate(sum=Sum('totalAmount'))

    context={'items':items_sorted,'amount':amount}
    return render(request, "summary.html",context)