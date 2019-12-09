from django.http import HttpResponse

from .models import Pizza


def index(request):
    return HttpResponse('Hello, Welcome to the Pizza Shop!')


def pizza_list(request):
    list_of_pizzas = []
    pizzas = Pizza.objects.values().order_by('-amount_sold')
    for pizza in pizzas:
        list_of_pizzas.append(pizza)
    return HttpResponse(list_of_pizzas)
