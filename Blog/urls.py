from django.urls import path,re_path
from . import views

urlpatterns = [
    
    path('',views.home,name="home"),
    path('contact/',views.contact,name="contact"),
    path('a propos/',views.about,name="about"),
    path('recherche/',views.searchbar,name="search"),
    path('category/<slug:category>/',views.home,name="category_home"),
    path('<slug:slug>/',views.detail,name="detail"),
    #re_path(r'^/$',views.search,name="search"),
]
