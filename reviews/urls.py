"""Restaurants URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

app_name = 'reviews'

urlpatterns = [
   
    url(r'^$', views.review_list, name='review_list'),
    
    url(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
    
    url(r'^restaurant$', views.restaurant_list, name='restaurant_list'),
    
    url(r'^restaurant/(?P<restaurant_id>[0-9]+)/$', views.restaurant_detail, name='restaurant_detail'),
    
    url(r'^review/user/(?P<username>\w+)/$', views.user_review_list, name='user_review_list'),
    #url(r'^restaurant/(?P<restaurant_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),
    url(r'^restaurant/(?P<restaurant_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),
]
