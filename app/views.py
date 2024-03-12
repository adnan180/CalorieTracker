from django.shortcuts import render, redirect
from .models import Food, Consume
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView


# Create your views here.
class FoodList(ListView):
    model = Food


def foodadd(req):
    if req.method == "GET":
        allfoods = Food.objects.all()
        consumed_food = Consume.objects.filter(user=req.user)
        context = {
            "allfoods": allfoods,
            "consumed_food": consumed_food,
        }
    else:
        food_consumed = req.POST["food_consumed"]
        selectedfood = Food.objects.get(name=food_consumed)
        consume = Consume(user=req.user, foodconsumed=selectedfood)
        consume.save()
        allfoods = Food.objects.all()
        consumed_food = Consume.objects.filter(user=req.user)
        context = {"consumed_food": consumed_food, "allfoods": allfoods}

    return render(req, "foodadd.html", context)


class FoodRegister(CreateView):
    model = Food
    fields = "__all__"
    success_url = "/FoodList"


class FoodRemove(DeleteView):
    model = Food
    success_url = "/FoodList"


class FoodUpdate(UpdateView):
    model = Food
    template_name_suffix = "_update_form"
    fields = "__all__"
    success_url = "/FoodList"


def index(req):
    allfood = Food.objects.all()
    context = {"allfood": allfood}
    return render(req, "index.html", context)


class FoodDetail(DetailView):
    model = Food


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def signin(req):
    if req.method == "POST":
        uname = req.POST["uname"]
        upass = req.POST["upass"]
        context = {}
        if uname == "" or upass == "":
            context["errmsg"] = "Field can't be empty"
            return render(req, "signin.html", context)
        else:
            userdata = authenticate(username=uname, password=upass)
            if userdata is not None:
                login(req, userdata)
                return redirect("/")
            else:
                context["errmsg"] = "Invalid username and password"
                return render(req, "signin.html", context)
    else:
        return render(req, "signin.html")


def userlogout(req):
    logout(req)
    return redirect("/")


def signup(req):
    if req.method == "POST":
        uname = req.POST["uname"]
        upass = req.POST["upass"]
        ucpass = req.POST["ucpass"]
        context = {}

        if uname == "" or upass == "" or ucpass == "":
            context["errmsg"] = "Field can't be empty"
            return render(req, "signup.html", context)
        elif upass != ucpass:
            context["errmsg"] = "Password and confirm password doesn't match"
            return render(req, "signup.html", context)
        else:
            try:
                userdata = User.objects.create(username=uname, password=upass)
                userdata.set_password(upass)
                userdata.save()
                return redirect("/signin")
            except:
                context["errmsg"] = "User Already exists"
                return render(req, "signup.html", context)
    else:
        context = {}
        context["errmsg"] = ""
        return render(req, "signup.html", context)
