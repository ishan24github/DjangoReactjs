from django.urls import path , re_path

from . import views

urlpatterns = [
    # path('', views.index),
    re_path(r'^(?:.*)/?$', views.index),
    # path('register', views.register),
    # path('startupForm', views.startupForm),
    # path('portfolio', views.portfolio),
]