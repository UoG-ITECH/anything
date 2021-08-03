from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify



class Category(models.Model):
    NAME_MAX_LENGTH = 128
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Page(models.Model):
    TITLE_MAX_LENGTH = 128
    URL_MAX_LENGTH = 200

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username

class Article(models.Model):
    title = models.CharField(max_length=300, help_text="Please enter the Article title here.")
    content = models.TextField(max_length=5000, help_text="Please enter the content of the article here.")
    date = models.DateField(help_text="Please enter the date here.")
    author = models.ForeignKey(UserProfile,on_delete=models.CASCADE, max_length=200, help_text="Please enter the author name here.")
    picture = models.ImageField(upload_to='article_images', blank=True)
    
    def __str__(self):
        return self.title

class Store(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    slug = models.SlugField(unique=True)
    ratings = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.name