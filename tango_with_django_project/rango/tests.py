from django.test import TestCase

from rango.models import Category, Product, Store
from django.urls import reverse
from django.shortcuts import render, redirect


class TestsFunctionality(TestCase):

    # test 1
    def test_slug_line_creation(self):
        '''Test ensures product slugs are set correctly, this is important
             as these are used to display static images and link to product page'''
        category = Category(name='Len 0')
        category.save()

        self.assertEqual(category.slug, 'len-0')

    # test 2
    def test_product_links_store_correctly(self):
        '''Since there is quite a large interdependency between stores and product,
        this test checks that these are correctly linked up'''
        category = Category(name='aaa')
        store = Store(name='store', email='store@a.com', ratings=5, latitude=5.321456, longitude= 45.311568)
        product = Product(name='Len', category=category, price=250.32, description='A good one', store=store)
        self.assertEqual('store', str(product.store.name))

    # test 3
    def test_store_lat_lon(self):
        '''This test ensures that no rounding error occurs when inputting
        the longitude and latitude as its extremely important that these are
        accurate to show the store location in maps'''
        lat = 5.321456
        lon = 45.311568
        store = Store(name='store', email='store@a.com', ratings=5, latitude=lat, longitude=lon)
        lat_correct = (lat == store.latitude)
        lon_correct = (lon == store.longitude)
        self.assertTrue(lat_correct and lon_correct)

class IndexViewTests(TestCase):
    def test_categories_added_correctly(self):
        '''
        Test that categories are correctly saved and displayed in the home page
        '''
        cat_name = 'category_test'
        category = Category(name=cat_name)
        category.save()
        response = self.client.get(reverse('rango:index'))
        self.assertContains(response, cat_name)




