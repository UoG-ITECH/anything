from django import template
from rango.models import Product

register = template.Library()


@register.simple_tag
def get_wishlist(request):
    wish_list = Product.objects.all()
    return wish_list
