from django.contrib import admin
from rango.models import Category, Product, UserProfile, DummyReview, Article, Store, Review
from django.conf import settings


class PageAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','latitude', 'longitude',)
    search_fields = ('name',)

    fieldsets = (
        (None, {
            'fields': ( 'name','email', 'latitude', 'longitude',)
        }),
    )

    class Media:
        if hasattr(settings, 'GOOGLE_MAPS_API_KEY') and settings.GOOGLE_MAPS_API_KEY:
            css = {
                'all': ('css/admin/location_picker.css',),
            }
            js = (
                'https://maps.googleapis.com/maps/api/js?key={}'.format(settings.GOOGLE_MAPS_API_KEY),
                'js/admin/location_picker.js',
            )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, PageAdmin)
admin.site.register(UserProfile)
admin.site.register(DummyReview)
admin.site.register(Review)
admin.site.register(Article)
