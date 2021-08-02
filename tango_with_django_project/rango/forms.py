from django import forms
from django.contrib.auth.models import User
from rango.models import Category, UserProfile, Product


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

    ram = forms.IntegerField(help_text="Please enter Product RAM")
    price = forms.FloatField(help_text="Please enter Product price")

    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    description = forms.CharField(widget=forms.Textarea, help_text="Enter Product description",
                                  max_length=Product.MAX_LEN_DESC)

    class Meta:
        model = Product
        exclude = ('category', 'slug')

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        # add http:// if not present
        if url and not url.startswith('http://'):
            url = f'http://{url}'
            cleaned_data['url'] = url

        return cleaned_data


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture',)
