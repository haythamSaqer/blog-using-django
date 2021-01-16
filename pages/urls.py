from django.urls import path, include  # new
from .views import homePageView
from . import views
urlpatterns = [

    path('', views.homePageView),  # new
]
