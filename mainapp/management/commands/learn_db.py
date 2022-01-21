from django.core.management.base import BaseCommand
from django.db import connection

from admins.views import db_profile_by_type
from mainapp.models import Product
from django.db.models import Q


class Command(BaseCommand):
    def handle(self, *args, **options):
        products = Product.objects.filter(
            ~Q(category__name='Обувь')
            # Q(category__name='Обувь')
            # ~Q(category__name='Обувь') | Q(category__name=1),
            # Q(category__name='Обувь') & Q(category__name=2),
        )
        print(len(products))
        db_profile_by_type('learn db', '', connection.queries)
        # print(products)
