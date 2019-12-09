# -*- encoding:utf-8 -*-
import datetime

from django.db import models
from django.utils import timezone


class PizzaType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Pizza(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=20, decimal_places=8, default=0)
    pizza_type = models.ForeignKey(PizzaType, on_delete=models.CASCADE)
    amount_sold = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Transactions(models.Model):
    pizza_id = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=20, decimal_places=8, default=0)

    def __str__(self):
        return self.pizza_id

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
