from django.contrib import admin
from django.urls import path
from .views import home, post, category, about, base

urlpatterns = [
        path('', base),
        path('home/', home),
        path('about/', about),
        path('blog/<slug:url>', post),
        path('category/<slug:url>', category)

]