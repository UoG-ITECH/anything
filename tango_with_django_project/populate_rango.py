import os
import pickle

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django

django.setup()
from rango.models import Category, Product, DummyReview, Store, Article
from django.contrib.auth.models import User, UserManager


def populate():
    """
    First, create the lists of dictionaries containing the pages we want to
    add to each category.
    Then we will create a dictionary for our categories.
    This might seem a little bit confusing, but it allows us to iterate through
    each data structure, and add data to our models
    """

    #TODO: Delete this before submission, will leave it for easier editing until then

    business = [
        {'name': 'Lenovo A340',
         'description': '''  All-in-One Design: The stunning A340 AIO PC will look great in any room with its elegant base and stand, this 21.5 Inch all-in-one takes up minimal space on your office desk
Exceptional viewing experience: With an adjustable near-edgeless 22-inch FHD WVA monitor, the A340 is perfect for comfortable working with a wider viewing angle for visual quality
Runs like a dream: Even when your workload gets hectic, the A340 multi-tasks seamlessly with Intel Core i3 processing, 4 GB DIMM DDR4 and 1 TB HDD storage
Your privacy counts: The IdeaCentre All-in-one enables you to livestream with ease while keeping your world private with a TrueBlock privacy shutter to hide your webcam whenever you want to
Keep organised: With a built-in cable tidy attached to the stand your desk stays clutter-free, even when you connect the bundled accessories - 1 x USB Calliope Keyboard and 1 x USB Calliope Mouse ''',
         'price': 600.97,
         'store': 'Slorten'
         },
        {'name': 'ASUS AiO',
         'description': ''' 23.8 inch Full HD IPS-level anti-glare display is the perfect solution to tackle everyday tasks
Windows 10 Home
AMD Ryzen 3 3250U Processor (5M Cache, up to 3.5 GHz)
8GB RAM and 256GB PCIe NVMe M.2 SSD
Flexible all-in-one weighing in at only 11.9 lb with 720p HD Video Camera ''',
         'price': 529.50,
         'store': 'Slorten'
         },
        {'name': 'Asus L210',
         'description': ''' Efficient Intel Celeron N4020 Processor (4M Cache, up to 2.8 GHz)
11.6” HD (1366 x 768) Slim Display
64GB eMMC Flash Storage and 4GB DDR4 RAM
Windows 10 in S Mode with One Year of Microsoft 365 Personal
Slim and Portable: 0.7” thin and weighs only 2.2 lbs (battery included) ''',
         'price': 260.50,
         'store': 'Slorten'
         },
        {'name': 'HP 14',
         'description': ''' POWER THROUGH FROM ANYWHERE – Designed to keep you productive and entertained from anywhere, the HP 14-inch Laptop combines long-lasting battery life with a thin and portable design
FULL HD DISPLAY – Enjoy your favorite content in 1080p for crystal-clear visuals and vibrant image quality. Beyond pixel count, your display lets you see more from anywhere thanks to the micro-edge bezel and anti-glare screen
INFINITE POSSIBILITIES – Whether you are creating, working, or being entertained, do it all with the supreme performance of the AMD Ryzen 5 5500U Mobile Processor and AMD Radeon Graphics
MEMORY AND STORAGE – Boost your performance with higher bandwidth, courtesy of 8 GB of RAM. Plus, with 256 GB PCIe NVMe M.2 SSD storage, save all of your photos, videos, and documents while getting up to 15x faster performance than a traditional hard drive ''',
         'price': 854.50,
         'store': 'Slorten'
         }
    ]

    portable = [
        {'name': 'Lenovo B900',
         'description': '''  All-in-One Design: The stunning A340 AIO PC will look great in any room with its elegant base and stand, this 21.5 Inch all-in-one takes up minimal space on your office desk
    Exceptional viewing experience: With an adjustable near-edgeless 22-inch FHD WVA monitor, the A340 is perfect for comfortable working with a wider viewing angle for visual quality
    Runs like a dream: Even when your workload gets hectic, the A340 multi-tasks seamlessly with Intel Core i3 processing, 4 GB DIMM DDR4 and 1 TB HDD storage
    Your privacy counts: The IdeaCentre All-in-one enables you to livestream with ease while keeping your world private with a TrueBlock privacy shutter to hide your webcam whenever you want to
    Keep organised: With a built-in cable tidy attached to the stand your desk stays clutter-free, even when you connect the bundled accessories - 1 x USB Calliope Keyboard and 1 x USB Calliope Mouse ''',
         'price': 349.99,
         'store': 'Slorten'},
        {'name': 'ASUS AYZ',
         'description': ''' 23.8 inch Full HD IPS-level anti-glare display is the perfect solution to tackle everyday tasks
    Windows 10 Home
    AMD Ryzen 3 3250U Processor (5M Cache, up to 3.5 GHz)
    8GB RAM and 256GB PCIe NVMe M.2 SSD
    Flexible all-in-one weighing in at only 11.9 lb with 720p HD Video Camera ''',
         'price': 749.50,
         'store': 'Slorten'
         },
        {'name': 'Asus M30',
         'description': ''' Efficient Intel Celeron N4020 Processor (4M Cache, up to 2.8 GHz)
    11.6” HD (1366 x 768) Slim Display
    64GB eMMC Flash Storage and 4GB DDR4 RAM
    Windows 10 in S Mode with One Year of Microsoft 365 Personal
    Slim and Portable: 0.7” thin and weighs only 2.2 lbs (battery included) ''',
         'price': 360.00,
         'store': 'Slorten'
         },
        {'name': 'HP 17 Laptop',
         'description': ''' POWER THROUGH FROM ANYWHERE – Designed to keep you productive and entertained from anywhere, the HP 14-inch Laptop combines long-lasting battery life with a thin and portable design
    FULL HD DISPLAY – Enjoy your favorite content in 1080p for crystal-clear visuals and vibrant image quality. Beyond pixel count, your display lets you see more from anywhere thanks to the micro-edge bezel and anti-glare screen
    INFINITE POSSIBILITIES – Whether you are creating, working, or being entertained, do it all with the supreme performance of the AMD Ryzen 5 5500U Mobile Processor and AMD Radeon Graphics
    MEMORY AND STORAGE – Boost your performance with higher bandwidth, courtesy of 8 GB of RAM. Plus, with 256 GB PCIe NVMe M.2 SSD storage, save all of your photos, videos, and documents while getting up to 15x faster performance than a traditional hard drive ''',
         'price': 900.50,
         'store': 'Sharon Elec.'
         }
    ]

    gaming = [
        {'name': 'Lenovo G4M3R',
         'description': '''  All-in-One Design: The stunning A340 AIO PC will look great in any room with its elegant base and stand, this 21.5 Inch all-in-one takes up minimal space on your office desk
        Exceptional viewing experience: With an adjustable near-edgeless 22-inch FHD WVA monitor, the A340 is perfect for comfortable working with a wider viewing angle for visual quality
        Runs like a dream: Even when your workload gets hectic, the A340 multi-tasks seamlessly with Intel Core i3 processing, 4 GB DIMM DDR4 and 1 TB HDD storage
        Your privacy counts: The IdeaCentre All-in-one enables you to livestream with ease while keeping your world private with a TrueBlock privacy shutter to hide your webcam whenever you want to
        Keep organised: With a built-in cable tidy attached to the stand your desk stays clutter-free, even when you connect the bundled accessories - 1 x USB Calliope Keyboard and 1 x USB Calliope Mouse ''',
         'price': 1349.99,
         'store': 'Slorten'},
        {'name': 'ASUS GZ',
         'description': ''' 23.8 inch Full HD IPS-level anti-glare display is the perfect solution to tackle everyday tasks
        Windows 10 Home
        AMD Ryzen 3 3250U Processor (5M Cache, up to 3.5 GHz)
        8GB RAM and 256GB PCIe NVMe M.2 SSD
        Flexible all-in-one weighing in at only 11.9 lb with 720p HD Video Camera ''',
         'price': 1749.50,
         'store': 'PC Universe Glasgow'
         },
        {'name': 'Asus GM3000',
         'description': ''' Efficient Intel Celeron N4020 Processor (4M Cache, up to 2.8 GHz)
        11.6” HD (1366 x 768) Slim Display
        64GB eMMC Flash Storage and 4GB DDR4 RAM
        Windows 10 in S Mode with One Year of Microsoft 365 Personal
        Slim and Portable: 0.7” thin and weighs only 2.2 lbs (battery included) ''',
         'price': 760.00,
         'store': 'Medium Market Glasgow'
         },
        {'name': 'HP 20 Gaming Laptop',
         'description': ''' POWER THROUGH FROM ANYWHERE – Designed to keep you productive and entertained from anywhere, the HP 14-inch Laptop combines long-lasting battery life with a thin and portable design
        FULL HD DISPLAY – Enjoy your favorite content in 1080p for crystal-clear visuals and vibrant image quality. Beyond pixel count, your display lets you see more from anywhere thanks to the micro-edge bezel and anti-glare screen
        INFINITE POSSIBILITIES – Whether you are creating, working, or being entertained, do it all with the supreme performance of the AMD Ryzen 5 5500U Mobile Processor and AMD Radeon Graphics
        MEMORY AND STORAGE – Boost your performance with higher bandwidth, courtesy of 8 GB of RAM. Plus, with 256 GB PCIe NVMe M.2 SSD storage, save all of your photos, videos, and documents while getting up to 15x faster performance than a traditional hard drive ''',
         'price': 600.50,
         'store': 'Gupta Appliances'
         }
    ]

    cats = {'Gaming': {'pages': gaming},
            'Business': {'pages': business},
            'Portable': {'pages': portable}}

    reviews= [
        {'user': 'Kevin89',
         'product': "ASUS AiO",
         'rating' : 10,
         'content': 'Thought it was an excellent machine! Works great for me.',
         'date': 'Jul. 11, 2021, 08:31 p.m.'},
        {'user': 'Kevin78',
         'product': "Lenovo A340",
         'rating': 8,
         'content': 'Thought it was a terrible machine! Works badly for me.',
         'date': 'Jun. 15, 2021, 03:31 a.m.'},
        {'user': 'Stac3y',
         'product': "Asus L210",
         'rating': 3,
         'content': 'Package arrived in very poor condition.',
         'date': 'Aug. 1, 2021, 03:31 p.m.'},
        {'user': 'Mark_Mills',
         'product': "Asus L210",
         'rating': 6,
         'content': 'Nothing fancy but it gets the job done I guess.',
         'date': 'Aug. 4, 2021, 05:01 a.m.'},
        {'user': 'stormbound',
         'product': "Asus L210",
         'rating': 7,
         'content': 'Great value! perfect if you are into music production!!',
         'date': 'Jul. 17, 2021, 07:31 p.m.'},
        {'user': 'Justin_95',
         'product': "Lenovo G4M3R",
         'rating': 8,
         'content': 'Amazing product! Gave me a chance to re-play Skyrim and I loved it on such a high end PC. Would '
                    'totally recommend',
         'date': 'Aug. 2, 2021, 07:00 p.m.'},
        {'user': 'Clar123',
         'product': "HP 20 Gaming Laptop",
         'rating': 5,
         'content': 'Its alright, but struggles to run some of my favourite games. Wish I would have grabbed '
                    'something a little better',
         'date': 'Jun. 1, 2021, 03:31 p.m.'},
        {'user': 'Stac3y',
         'product': "HP 17 Laptop",
         'rating': 9,
         'content': 'Excellent! My daughter loved it!',
         'date': 'Jun. 10, 2021, 04:31 a.m.'},
        {'user': 'Frankie_A',
         'product': "Lenovo G4M3R",
         'rating': 10,
         'content': 'Won plenty of games with this bad boy, would totally recommend. Is great for video editing too!',
         'date': 'Jul. 21, 2021, 09:38 p.m.'},
        {'user': 'El_Fijo',
         'product': "ASUS GZ",
         'rating': 10,
         'content': 'Incredible, did not think computer graphics could look this good',
         'date': 'Aug. 1, 2021, 03:31 p.m.'},
        {'user': 'Mike_L',
         'product': "ASUS AYZ",
         'rating': 3,
         'content': 'More like AY it Zucks lol',
         'date': 'Aug. 3, 2021, 11:31 p.m.'},
        {'user': 'Stefan_1K',
         'product': "Asus M30",
         'rating': 5,
         'content': 'It is ok. No further comments.',
         'date': 'Jun. 19, 2021, 04:31 p.m.'},


    ]

    stores = [
        {
            'name': 'Medium Market Glasgow',
            'email': 'mm@mm.com',
            'latitude' : 55.877150,
            'longitude': -4.224912,
            'rating': 7,
        },
        {
            'name': 'PC Universe Glasgow',
            'email': 'pcu@pcu.com',
            'latitude': 54.264264,
            'longitude': -5.234167,
            'rating': 3,
        },
        {
            'name': 'Slorten',
            'email': 'slor@ten.com',
            'latitude': 55.977150,
            'longitude': -4.424912,
            'rating': 10,
        },
        {
            'name': 'Sharon Elec.',
            'email': 'sharonelec@gmail.com',
            'latitude': 55.577150,
            'longitude': -4.324912,
            'rating': 9,
        },
        {
            'name': 'Gupta Appliances',
            'email': 'guptaApp@hotmail.com',
            'latitude': 55.977150,
            'longitude': -4.124912,
            'rating': 6,
        },
    ]
    li = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Bibendum neque egestas congue quisque egestas diam in arcu. Tincidunt praesent semper feugiat nibh sed pulvinar proin gravida. Enim ut sem viverra aliquet eget sit. Ipsum dolor sit amet consectetur adipiscing elit pellentesque habitant. Id nibh tortor id aliquet lectus. Sit amet venenatis urna cursus. Mauris commodo quis imperdiet massa tincidunt. Tellus rutrum tellus pellentesque eu tincidunt tortor aliquam nulla. Adipiscing elit pellentesque habitant morbi tristique senectus.

Ullamcorper sit amet risus nullam eget. Neque convallis a cras semper auctor neque. Ac odio tempor orci dapibus ultrices. Donec massa sapien faucibus et molestie ac feugiat sed. Justo eget magna fermentum iaculis eu non. Diam vulputate ut pharetra sit. Rutrum quisque non tellus orci ac auctor. Quam viverra orci sagittis eu volutpat odio facilisis mauris. Et egestas quis ipsum suspendisse ultrices. Tempor nec feugiat nisl pretium fusce. Ipsum dolor sit amet consectetur adipiscing elit ut aliquam purus. Mollis aliquam ut porttitor leo a diam sollicitudin tempor id. Amet massa vitae tortor condimentum. Sed euismod nisi porta lorem mollis aliquam. Cursus vitae congue mauris rhoncus aenean.

Leo a diam sollicitudin tempor id eu nisl nunc. Volutpat sed cras ornare arcu dui vivamus arcu. Imperdiet dui accumsan sit amet nulla. Egestas quis ipsum suspendisse ultrices gravida. Enim sit amet venenatis urna cursus eget. Ultrices mi tempus imperdiet nulla malesuada pellentesque. Sed velit dignissim sodales ut eu sem. Massa eget egestas purus viverra. Varius vel pharetra vel turpis. Vitae justo eget magna fermentum iaculis. Arcu cursus euismod quis viverra nibh cras pulvinar. Ultrices tincidunt arcu non sodales. Elit duis tristique sollicitudin nibh sit amet commodo nulla. Curabitur gravida arcu ac tortor dignissim.

Faucibus purus in massa tempor nec feugiat nisl. Est ullamcorper eget nulla facilisi etiam. Ut lectus arcu bibendum at varius vel pharetra vel turpis. A arcu cursus vitae congue mauris. Id neque aliquam vestibulum morbi blandit cursus. Massa placerat duis ultricies lacus sed turpis tincidunt. Lorem sed risus ultricies tristique nulla. A diam maecenas sed enim ut sem viverra aliquet eget. Mattis pellentesque id nibh tortor id aliquet lectus proin nibh. Enim sit amet venenatis urna cursus eget. Eget dolor morbi non arcu. Aliquet nibh praesent tristique magna sit amet purus gravida quis. Adipiscing tristique risus nec feugiat. Sollicitudin nibh sit amet commodo nulla facilisi nullam vehicula ipsum. Amet dictum sit amet justo donec enim diam vulputate ut. At risus viverra adipiscing at in tellus integer feugiat scelerisque. Eget est lorem ipsum dolor. A lacus vestibulum sed arcu. Nisi scelerisque eu ultrices vitae auctor eu. Ullamcorper eget nulla facilisi etiam.

Euismod in pellentesque massa placerat duis. Risus pretium quam vulputate dignissim suspendisse in est ante in. Ac turpis egestas maecenas pharetra convallis posuere morbi leo urna. Metus dictum at tempor commodo ullamcorper. Mauris vitae ultricies leo integer malesuada nunc vel risus. Morbi tristique senectus et netus et malesuada fames ac turpis. Mauris in aliquam sem fringilla ut morbi tincidunt. Praesent semper feugiat nibh sed pulvinar proin gravida hendrerit. Facilisi cras fermentum odio eu. Purus gravida quis blandit turpis cursus in hac habitasse. Vitae tortor condimentum lacinia quis vel eros donec ac odio."""
    articles = [
        {'title': 'The latest from Lenovo and my thoughts on it',
        'content': li,
    'author': 'Frozen_raspberry'
    },
        {'title': 'HP 17: My opinion',
         'content': li,
         'author': 'Steven_M'
         },

        {'title': 'First impressions on my new Apple Computer',
         'content': li,
                    'author': 'Joyce05'
         },
        {'title': 'Mini Gaming computers, are we there yet?',
         'content': li,
         'author': 'Parvati01'
         }
    ]

    comps = [cats, reviews, stores, articles]
    # This will pickle all the above data and put it in population_data
    filename = 'population_data'
    outfile = open(filename,'wb')
    pickle.dump(comps,outfile)
    outfile.close()

    # reads population_data and outputs the contents
    filename = 'population_data'
    infile = open(filename, 'rb')
    new_dict = pickle.load(infile)
    infile.close()

    cats = new_dict[0]
    reviews = new_dict[1]
    stores = new_dict[2]
    articles = new_dict[3]

    for store in stores:
        add_store(store['name'], store['email'], store['latitude'], store['longitude'], store['rating'])
    # The code below goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category.

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data['pages']:
            add_product(c, p['name'],  p['price'], p['description'], p['store'])

    # Print out the categories we have added.
    for c in Category.objects.all():
        for p in Product.objects.filter(category=c):
            print(f'- {c}: {p}')

    for review in reviews:
        add_review(review['user'], review['product'], review['rating'], review['content'], review['date'] )

    for article in articles:
        add_article(article['title'], article['content'], article['author'])











def add_product(cat, name, price, description, store):
    p = Product.objects.get_or_create(category=cat, name=name)[0]
    p.price = price
    p.description = description
    p.store = Store.objects.get_or_create(name=store)[0]
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

def add_store(name, email,latitude, longitude, ratings):
    s = Store.objects.get_or_create(name=name,email=email, latitude=latitude, longitude=longitude, ratings=ratings)[0]
    s.save()
    return s

def add_article(title, content, author):
    user = User.objects.get_or_create(username=author,password='bobspassword')[0]

    a = Article.objects.get_or_create(title=title, content=content, author=user)[0]
    a.save()
    return a



if __name__ == '__main__':
    print("Starting rango population script...")
    populate()
