from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('contact_us/', views.contactus_view, name='contact_us'),
    path('about_us/', views.about_us, name='about_us'),
    path('register/', views.registerPage, name='register'),
    path('accounts/login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('directions/', views.directions, name='directions'),
    path('places/', views.places, name='places'),
    path('city/', views.city, name='city'),
    path('planner/', views.planner.as_view(), name='planner'),
    path('todolist/', views.todolist.as_view(), name='todolist'),
    path('createplan/', views.createplan.as_view(), name='createplan'),
    path('updateplan/<id>/', views.updateplan, name='updateplan'),
    path('createreview/', views.createreview.as_view(), name='createreview'),
    path('createtask/', views.createtask.as_view(), name='createtask'),
    path('deleteplan/<id>/', views.deleteplan, name='deleteplan'),
    path('deletetask/<id>/', views.deletetask, name='deletetask'),
    path('updatetask/<id>/', views.updatetask, name='updatetask'),
]
