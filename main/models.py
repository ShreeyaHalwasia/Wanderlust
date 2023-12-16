from django.db import models
from django.urls import reverse
# Create your models here.


class Planner(models.Model):
    PRI_CHOICES = (
        ("High", "High"),
        ("Medium", "Medium"),
        ("Low", "Low")
    )
    destination = models.CharField(max_length=100)
    budget = models.IntegerField()
    priority = models.CharField(max_length=20, choices=PRI_CHOICES)
    date = models.DateField()
    travelbag = models.CharField(max_length=200)
    note = models.CharField(max_length=1000)
    Status = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("planner")

    def __str__(self):
        return f"{self.destination}" or ""


class ToDoList(models.Model):
    task = models.CharField(max_length=100)
    plan = models.ForeignKey(Planner, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("todolist")


class Reviews(models.Model):
    RATING_CHOICES = (
        ("Awesome", "Awesome"),
        ("Very Good", "Very Good"),
        ("Good", "Good"),
        ("Not Bad", "Not Bad"),
        ("Bad", "Bad"),
    )
    review = models.CharField(max_length=4000)
    rating = models.CharField(max_length=20, choices=RATING_CHOICES)

    def get_absolute_url(self):
        return reverse("home")