import os
import random
import django
from random import choice



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from faker import Faker
from main import models

models.Bigcategory.objects.all().delete()
models.SmallCategory.objects.all().delete()
models.Product.objects.all().delete()

fake = Faker()


for _ in range(10):
    big_categories = models.Bigcategory.objects.create(
        name = random.choice([choice.value for choice in models.BigCategories])

    )
    big_categories.save()
models.Bigcategory.objects.all()
print('Add big_categories')


for _ in range(40):
    small_categories = models.SmallCategory.objects.create(
        big_category = choice(models.Bigcategory.objects.all()),
        
        name = random.choice([choice.value for choice in models.SmallCategories])
    )
    small_categories.save()
models.SmallCategory.objects.all()
print('Add small_categories')


for _ in range(100):
    products = models.Product.objects.create(
        big_category = choice(models.Bigcategory.objects.all()),

        small_category = choice(models.SmallCategory.objects.all()),
        name = fake.word().capitalize(),
        price = round(random.uniform(500, 1500000), 2),
        description = fake.text().capitalize(),
        brand = fake.word().capitalize(),
        color = fake.color().capitalize(),
        material = fake.word().capitalize(),
        country_of_origin = fake.state().capitalize(),
        warranty = fake.text().capitalize(),
        availability = fake.boolean(),
        rating = round(random.uniform(1, 10), 2),
        discount = round(random.uniform(20, 90), 1),
        stock_quantity = round(random.uniform(1, 100)),
        tags = fake.text().capitalize()


    )