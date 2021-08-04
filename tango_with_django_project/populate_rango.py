import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django

django.setup()
from rango.models import Category, Product, DummyReview


def populate():
    """
    First, create the lists of dictionaries containing the pages we want to
    add to each category.
    Then we will create a dictionary for our categories.
    This might seem a little bit confusing, but it allows us to iterate through
    each data structure, and add data to our models
    """

    desc = " The new Computer Released by BRAND is incredible and offers some amazing Capabilities" \
           "RAM: 16" \
           "GPU: 1660 Super" \
           "Processor: 9780 i7"

    business = [
        {'name': 'Asus 2',
         'url': 'http://docs.python.org/3/tutorial/',
         'description': desc,
         'price': 600.50},
        {'name': 'Asus 3',
         'url': 'http://www.greenteapress.com/thinkpython/',
         'description': desc,
         'price': 560.50,
         },
        {'name': 'Asus 5',
         'url': 'http://www.korokithakis.net/tutorials/python/',
         'description': desc,
         'price': 480.50
         }]

    portable = [
        {'name': 'Asus 6',
         'url': 'http://docs.python.org/3/tutorial/',
         'description': desc,
         'price': 800.50},
        {'name': 'Asus 7',
         'url': 'http://www.greenteapress.com/thinkpython/',
         'description': desc,
         'price': 600.50
         },
        {'name': 'Asus 8',
         'url': 'http://www.korokithakis.net/tutorials/python/',
         'description': desc,
         'price': 300.50
         }
    ]

    gaming = [
        {'name': 'Asus 9',
         'url': 'http://docs.python.org/3/tutorial/',
         'description': desc,
         'price': 1600.50
         },
        {'name': 'Asus 10',
         'url': 'http://www.greenteapress.com/thinkpython/',
         'description': desc,
         'price': 1000.50
         },
        {'name': 'Asus 11',
         'url': 'http://www.korokithakis.net/tutorials/python/',
         'description': desc,
         'price': 800.50
         }]

    cats = {'Gaming': {'pages': gaming},
            'Business': {'pages': business},
            'Portable': {'pages': portable}}

    # The code below goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category.

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data['pages']:
            add_product(c, p['name'], p['url'], p['price'], p['description'])

    # Print out the categories we have added.
    for c in Category.objects.all():
        for p in Product.objects.filter(category=c):
            print(f'- {c}: {p}')

    add_review("jeff08", "Asus 11", 8, "Very good!", "Aug. 1, 2021, 7:41 p.m.")
    add_review("jeff04", "Asus 2", 2, "Very bad!", "Jul. 21, 2021, 11:01 p.m.")


def add_product(cat, name, url, price, description):
    p = Product.objects.get_or_create(category=cat, name=name)[0]
    p.url = url

    p.price = price
    p.description = description

    p.save()
    return p


def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]

    c.save()
    return c


def add_review(user, product, rating, content, date):
    prd = Product.objects.get(name=product)
    p = DummyReview.objects.get_or_create(dummy_product=prd,dummy_user=user, dummy_date=date, dummy_rating=rating,
                                          dummy_content=content)[0]

    p.save()
    return p



if __name__ == '__main__':
    print("Starting rango population script...")
    populate()
