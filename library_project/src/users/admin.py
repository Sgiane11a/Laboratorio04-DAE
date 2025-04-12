from django.contrib import admin
from .models import LibraryUser, ReadingList, BookReview


@admin.register(LibraryUser)
class LibraryUserAdmin(admin.ModelAdmin):
    """Configuración del panel de administración para LibraryUser"""
    list_display = ('username', 'email', 'is_staff', 'is_active')  # Campos visibles en la lista
    list_filter = ('is_staff', 'is_active')  # Filtros laterales
    search_fields = ('username', 'email')  # Campos de búsqueda
    ordering = ('username',)  # Orden predeterminado


@admin.register(ReadingList)
class ReadingListAdmin(admin.ModelAdmin):
    """Configuración del panel de administración para ReadingList"""
    list_display = ('name', 'user', 'is_public', 'created_at')  # Campos visibles en la lista
    list_filter = ('is_public', 'created_at')  # Filtros laterales
    search_fields = ('name', 'user__username')  # Campos de búsqueda
    ordering = ('-created_at',)  # Orden predeterminado


@admin.register(BookReview)
class BookReviewAdmin(admin.ModelAdmin):
    """Configuración del panel de administración para BookReview"""
    list_display = ('book', 'user', 'rating', 'created_at')  # Campos visibles en la lista
    list_filter = ('rating', 'created_at')  # Filtros laterales
    search_fields = ('book__title', 'user__username')  # Campos de búsqueda
    ordering = ('-created_at',)  # Orden predeterminado