from django.shortcuts import render, get_object_or_404
from .models import LibraryUser, ReadingList, BookReview


def user_list(request):
    """Vista para listar todos los usuarios"""
    users = LibraryUser.objects.all()
    return render(request, 'users/user_list.html', {'users': users})


def user_detail(request, pk):
    """Vista para mostrar detalles de un usuario"""
    user = get_object_or_404(LibraryUser, pk=pk)
    return render(request, 'users/user_detail.html', {'user': user})


def user_reading_lists(request, pk):
    """Vista para mostrar las listas de lectura de un usuario"""
    user = get_object_or_404(LibraryUser, pk=pk)
    reading_lists = user.reading_lists.all()
    return render(request, 'users/user_reading_lists.html', {'user': user, 'reading_lists': reading_lists})


def user_reviews(request, pk):
    """Vista para mostrar las reseñas de un usuario"""
    user = get_object_or_404(LibraryUser, pk=pk)
    reviews = user.reviews.all()
    return render(request, 'users/user_reviews.html', {'user': user, 'reviews': reviews})