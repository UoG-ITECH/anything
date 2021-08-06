from django.urls import path, include
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('category/<slug:category_name_slug>/', views.ShowCategoryView.as_view(), name='show_category'),
    path('category/<slug:category_name_slug>/add_product/', views.AddProductView.as_view(), name='add_product'),
    path('add_category/', views.AddCategoryView.as_view(), name='add_category'),
    path('restricted/', views.restricted, name='restricted'),

    path('search/', views.search, name='search'),
    path('product/<slug>/', views.ShowProductView.as_view(), name='show_computer'),
    path('product/<slug>/review/', views.AddReviewView.as_view(), name='review'),
    path('register_profile/', views.register_profile, name='register_profile'),
    path('register/', views.register, name='register'),
    path('profile/', views.ProfileView.as_view(), name='profile'),


    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('add_article/', views.add_article, name="add_article"),
    path('article/', views.article_show, name="article_show"),
    path('edit_article/<str:pk>/', views.edit_article, name="edit_article"),
    path('delete_article/<str:pk>/', views.delete_article, name="delete_article"),
    path('store/', views.store_show, name="store_show"),
    path('wishlist_view/', views.wishlist_view, name="wishlist_view"),
    path('add_wishlist/<int:id>', views.add_wishlist_view, name="add_wishlist_view"),
    # path('add_wishlist/', views.add_wishlist, name="add_wishlist"),
    path('article_view/', views.article_view, name="article_view"),
    path('article_information/<str:pk>/', views.article_information, name="article_information"),
    path('store_information/<str:pk>/', views.store_information, name="store_information"),
]