from django.contrib import admin
from rango.models import Category, Product, UserProfile, DummyReview, Article, Store


class PageAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}



admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, PageAdmin)
admin.site.register(UserProfile)
admin.site.register(DummyReview)
admin.site.register(Article)
admin.site.register(Store)