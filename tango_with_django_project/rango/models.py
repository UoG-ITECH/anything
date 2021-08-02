from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    MAX_LEN_NAME = 128
    name = models.CharField(max_length=MAX_LEN_NAME, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    # Denotes Max length of title and description variables
    MAX_LEN_TITLE = 128
    MAX_LEN_DESC = 50000


    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=MAX_LEN_TITLE)
    price = models.FloatField(default=0)
    description = models.TextField(max_length=MAX_LEN_DESC, default='')
    slug = models.SlugField()
    picture = models.ImageField(upload_to='product_images', blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
