from django.contrib import admin

from .models import PizzaType, Pizza, Transactions

# Register your models here.
admin.site.register(PizzaType)
admin.site.register(Pizza)
admin.site.register(Transactions)

