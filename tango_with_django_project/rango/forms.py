from django import forms
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from rango.models import Category, UserProfile, Product, Review




class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=Category.MAX_LEN_NAME,
                           help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)


class ProductForm(forms.ModelForm):
    MAX_LEN_URL = 200
    name = forms.CharField(max_length=Product.MAX_LEN_TITLE,
                           help_text="Please enter the Product name.")
    price = forms.FloatField(help_text="Please enter Product price",
                             validators=[MinValueValidator(0)]
                             )
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    description = forms.CharField(widget=forms.Textarea, help_text="Enter Product description",
                                  max_length=Product.MAX_LEN_DESC)
    picture = forms.ImageField(help_text="Submit a picture of the product",required=False)

    class Meta:
        model = Product
        exclude = ('category', 'slug')




class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture',)


class ReviewForm(forms.ModelForm):
    rating = forms.IntegerField(validators=[MinValueValidator(0),
                                            MaxValueValidator(10)], help_text="Enter Rating out of 10")
    content = forms.CharField(widget=forms.Textarea, help_text="Enter Product description",
                              max_length=Review.MAX_LEN_CONTENT)

    class Meta:
        model = Review
        exclude = ('user', 'product', 'date')
