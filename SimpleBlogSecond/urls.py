from django.urls import path
from .views import blog_view

urlpatterns = [
    path('BlogWebsite', blog_view),
]
