from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.user_list, name='user_list'),  # Lista de usuarios
    path('<int:pk>/', views.user_detail, name='user_detail'),  # Detalle de usuario
    path('<int:pk>/reading-lists/', views.user_reading_lists, name='user_reading_lists'),  # Listas de lectura
    path('<int:pk>/reviews/', views.user_reviews, name='user_reviews'),  # Reseñas de usuario
]