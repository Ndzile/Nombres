from django.urls import path
from . import views

# app_name = 'Nombres'  # Name for your application

urlpatterns = [
    path('', views.connexion, name='connexion'),
    path('dash/', views.dash, name='dash'),
    path('bureau-regional/creer/', views.creer_membre_bureau_regional, name='creer_membre_bureau_regional'),
    path('coordination_locale/creer/', views.creer_membre_coordination_locale, name='creer_membre_coordination_locale'),
    path('coordination_locale/<int:id>/membres/', views.membres_coordination_locale, name='membres_coordination_locale'),
    path('bureau_regional/<int:id>/membres/', views.membres_bureau_regional, name='membres_bureau_regional'),
    path('signout', views.signout, name='signout'),
    # Add more URL patterns here for other functionalities (optional)
]
