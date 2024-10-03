"""
URL configuration for Afisha project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from movie_app import views

urlpatterns = [
    path('api/v1/directors/', views.DirectorList.as_view(), name='director-list'),
    path('api/v1/directors/<int:pk>/', views.DirectorDetail.as_view(), name='director-detail'),
    path('api/v1/movies/', views.MovieList.as_view(), name='movie-list'),
    path('api/v1/movies/<int:pk>/', views.MovieDetail.as_view(), name='movie-detail'),
    path('api/v1/reviews/', views.ReviewList.as_view(), name='review-list'),
    path('api/v1/reviews/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail'),
]
