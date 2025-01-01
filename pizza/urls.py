from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns=[
    path("",views.home,name="home"),
    path("order",views.order,name="order"),
    path("pizzas",views.pizzas,name="pizzas"),
    path("order/<int:pk>",views.edit_order,name="edit_order")
]