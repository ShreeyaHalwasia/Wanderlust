from django.shortcuts import render, redirect
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from .api_utils import get_trip_plan, get_city_location_code, get_hotels_info
from django.contrib import messages
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from .forms import CreateUserForm, CreatePlanForm, CreateTaskForm, CreateReviewForm
from .models import Planner, ToDoList, Reviews

from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

from django.core.mail import send_mail
# Create your views here.


@login_required
def home_view(request):
    context = {}
    context["reviewform"] = CreateReviewForm()
    context["reviews"] = Reviews.objects.all()
    template = "home.html"
    print(f"DAYS:{request.POST.get('days')}")
    if (request.POST.get('days')):
        days1 = request.POST.get('days')
        print(request.POST.get('days'))
        location1 = request.POST.get('location')
        print(request.POST.get('location'))

        body = {
            "days": days1,
            "destination": location1
        }
        context["tplan"] = get_trip_plan(body)
        return render(request, template, context)
    else:
        return render(request, template, context)


def contactus_view(request):
    context = {}
    template = "contactus.html"
    if request.method == "POST":
        message_name = request.POST['message_name']
        message_email = request.POST['message_email']
        message = request.POST['message']

        send_mail(
            message_name,
            message,
            message_email,
            ['gokukakarot888888@gmail.com'],
            fail_silently=False,
        )
        context = {
            "prompt": "Your Mail was sent successfully!"
        }
        return render(request, template, context)
    return render(request, template, context)


class createplan(CreateView):
    model = Planner
    form_class = CreatePlanForm


class createreview(CreateView):
    print("inside createreview")
    model = Reviews
    form_class = CreateReviewForm


def deleteplan(request, id):
    obj = get_object_or_404(Planner, id=id)
    obj.delete()
    return redirect('/planner')


class createtask(CreateView):
    model = ToDoList
    form_class = CreateTaskForm


def deletetask(request, id):
    obj = get_object_or_404(ToDoList, id=id)
    obj.delete()
    return redirect('/todolist')


def updatetask(request, id):
    obj = get_object_or_404(ToDoList, id=id)
    obj.status = True
    obj.save()
    return redirect('/todolist')


def updateplan(request, id):
    obj = get_object_or_404(Planner, id=id)
    obj.Status = True
    obj.save()
    return redirect('/planner')


class planner(ListView):
    model = Planner
    template_name = "planner.html"

    def get_context_data(self, **kwargs):
        context = super(planner, self).get_context_data()
        """ 
        the basic object will be object_list
        With generic class based view on the listview and the detailview
        you can supercharge the context to make object available in templates
        'as seen bellow if I use {{available_variable_in_template }} in the 
        templates it will render Hello world 
        """
        context["planform"] = CreatePlanForm()
        return context


class todolist(ListView):
    model = ToDoList
    template_name = "todolist.html"

    def get_context_data(self, **kwargs):
        context = super(todolist, self).get_context_data()
        """ 
        the basic object will be object_list
        With generic class based view on the listview and the detailview
        you can supercharge the context to make object available in templates
        'as seen bellow if I use {{available_variable_in_template }} in the 
        templates it will render Hello world 
        """
        context["todolistform"] = CreateTaskForm()
        return context


def directions(request):
    context = {}
    template = "directions.html"
    return render(request, template, context)


def about_us(request):
    context = {}
    template = "aboutus.html"
    return render(request, template, context)


def places(request):
    context = {
        "keywordtype": request.POST.get('searchInput')
    }

    template = "places.html"
    return render(request, template, context)


def city(request):
    context = {}
    template = "city.html"
    print(f"CITY:{request.POST.get('city')}")
    if (request.POST.get('city')):
        city1 = request.POST.get('city')
        checkin = request.POST.get('checkin')
        checkout = request.POST.get('checkout')
        print(request.POST.get('city'))
        print(checkin)
        print(checkout)
        body = {
            "name": city1,
            "locale": 'en-gb'
        }
        city_details = get_city_location_code(body)
        x = json.dumps(city_details)
        y = json.loads(x)
        dest_id = y[0]['dest_id']
        print(dest_id)
        querystring = {
            "checkin_date": checkin,
            "dest_type": "city",
            "units": "metric",
            "checkout_date": checkout,
            "adults_number": "2",
            "order_by": "popularity",
            "dest_id": dest_id,
            "filter_by_currency": "INR",
            "locale": "en-gb",
            "room_number": "1",
            "children_number": "2",
            "children_ages": "5,0",
            "categories_filter_ids": "class::2,class::4,free_cancellation::1",
            "page_number": "0",
            "include_adjacency": "true",
        }
        print("HOTELS INFO-------")
        hotels_info = get_hotels_info(querystring)
        context = {
            'info': hotels_info,
        }

        return render(request, template, context)
    else:
        return render(request, template, context)


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, "Account was created " + user)
            return redirect("/accounts/login")

    context = {"form": form}
    return render(request, "register.html", context)


@unauthenticated_user
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Username or Password is incorrect!")

    context = {}
    return render(request, "login.html", context)


def logoutUser(request):
    logout(request)
    return redirect("/accounts/login")


def my_backend_view(request):
    template = "home.html"
    context = {}
    days1 = request.POST.get('days')
    location1 = request.POST.get('location')

    body = {
        "days": days1,
        "destination": location1
    }
    context["tplan"] = get_trip_plan(body)
    return render(request, template, context)
