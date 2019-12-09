# -*- encoding:utf-8 -*-
import random
from django.core.management.base import BaseCommand, CommandError
from pizza_app.models import Pizza


class Command(BaseCommand):
    def __init__(self):
        super().__init__()
        self.randomizer = random.randint(0, 100) % 3

    def handle(self, *args, **options):
        new = Pizza(name='Random Pizza', pizza_type_id=self.randomizer + 3,
                    price=99*(self.randomizer + 3),
                    amount_sold=random.randint(0, 100))
        new.save()
