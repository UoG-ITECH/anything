from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('category/<slug:category_name_slug>/', views.ShowCategoryView.as_view(), name='show_category'),
    path('category/<slug:category_name_slug>/add_product/', views.AddProductView.as_view(), name='add_product'),
    path('add_category/', views.AddCategoryView.as_view(), name='add_category'),
    path('restricted/', views.restricted, name='restricted'),
    path('goto/', views.goto_url, name='goto'),
    path('search/', views.search, name='search'),
    path('product/<slug>/', views.ShowProductView.as_view(), name='show_computer'),
    path('product/<slug>/review/', views.AddReviewView.as_view(), name='review'),
    path('register_profile/', views.register_profile, name='register_profile'),
    path('register/', views.register, name='register'),
    path('profile/', views.ProfileView.as_view(), name='profile'),

    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

]