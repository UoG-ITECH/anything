import os
import pickle

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
         'description': desc,
         'price': 600.50},
        {'name': 'Asus 3',
         'description': desc,
         'price': 560.50,
         },
        {'name': 'Asus 5',
         'description': desc,
         'price': 480.50
         },
        {'name': 'Asus 15',
         'description': desc,
         'price': 854.50
         }
    ]

    portable = [
        {'name': 'Asus 6',
         'description': desc,
         'price': 800.50},
        {'name': 'Asus 7',
         'description': desc,
         'price': 600.50
         },
        {'name': 'Asus 8',
         'description': desc,
         'price': 300.50
         }
    ]

    gaming = [
        {'name': 'Asus 9',
         'description': desc,
         'price': 1600.50
         },
        {'name': 'Asus 10',
         'description': desc,
         'price': 1000.50
         },
        {'name': 'Asus 11',
         'description': desc,
         'price': 800.50
         }]

    cats = {'Gaming': {'pages': gaming},
            'Business': {'pages': business},
            'Portable': {'pages': portable}}

    reviews= [
        {'user': 'Kevin89',
         'product': "Asus 15",
         'rating' : 10,
         'content': 'Thought it was an excellent machine! Works great for me.',
         'date': 'Jul. 11, 2021, 08:31 p.m.'},
        {'user': 'Kevin78',
         'product': "Asus 15",
         'rating': 8,
         'content': 'Thought it was a terrible machine! Works badly for me.',
         'date': 'Jun. 15, 2021, 03:31 a.m.'},

    ]

    comps = [cats, reviews]

    filename = 'population_data'
    outfile = open(filename,'wb')
    pickle.dump(comps,outfile)
    outfile.close()
    infile = open(filename, 'rb')
    new_dict = pickle.load(infile)
    infile.close()

    cats = new_dict[0]
    reviews = new_dict[1]

    # The code below goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category.

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data['pages']:
            add_product(c, p['name'],  p['price'], p['description'])

    # Print out the categories we have added.
    for c in Category.objects.all():
        for p in Product.objects.filter(category=c):
            print(f'- {c}: {p}')

    for review in reviews:
        add_review(review['user'], review['product'], review['rating'], review['content'], review['date'] )

    add_review("jeff08", "Asus 11", 8, "Very good!", "Aug. 1, 2021, 7:41 p.m.")
    add_review("jeff04", "Asus 2", 2, "Very bad!", "Jul. 21, 2021, 11:01 p.m.")


def add_product(cat, name, price, description):
    p = Product.objects.get_or_create(category=cat, name=name)[0]
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
