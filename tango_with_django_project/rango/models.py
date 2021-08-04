from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.template.defaultfilters import last, slugify


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

class Store(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    slug = models.SlugField(unique=True)
    ratings = models.IntegerField(default=0)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Store, self).save(*args, **kwargs)

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
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True)

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
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.username


# Handles customer reviews
class Review(models.Model):
    '''
    Rating and content are set by the user
    Product is set through slug
    Date is set automatically on posting
    User is obtained from request
    '''
    MAX_LEN_CONTENT = 50000

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(0),
                                             MaxValueValidator(10)])
    content = models.TextField(max_length=MAX_LEN_CONTENT, default='')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + " Reviewed " + self.product.name + " " + str(self.rating) + "/10" \
               + " Saying: " + self.content


class DummyReview(models.Model):
    '''
    Dummy review class used to populate the page with existing reviews
    '''
    dummy_user = models.TextField()
    dummy_product = models.ForeignKey(Product, related_name='dummy_reviews', on_delete=models.CASCADE)
    dummy_rating = models.IntegerField(blank=True)
    dummy_content= models.TextField()
    dummy_date = models.TextField()


class Article(models.Model):
    title = models.CharField(max_length=300, help_text="Please enter the Article title here.")
    content = models.TextField(max_length=5000, help_text="Please enter the content of the article here.")
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE, max_length=200)
    picture = models.ImageField(upload_to='article_images', blank=True)

    def __str__(self):
        return self.title

