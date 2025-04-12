from django.db import models
from django.contrib.auth.models import AbstractUser
from library.models import Book, Category  # Importamos modelos existentes

# Modelo para extender el usuario predeterminado de Django
class LibraryUser(AbstractUser):
    """Modelo de usuario extendido con campos adicionales"""
    bio = models.TextField(blank=True, null=True)  # Biografía del usuario
    favorite_categories = models.ManyToManyField(
        Category, blank=True, related_name='fans'
    )  # Categorías favoritas
    profile_image = models.ImageField(
        upload_to='user_profiles/', blank=True, null=True
    )  # Imagen de perfil

    def __str__(self):
        return self.username


# Modelo para listas de lectura
class ReadingList(models.Model):
    """Modelo para listas de lectura de los usuarios"""
    user = models.ForeignKey(
        LibraryUser, on_delete=models.CASCADE, related_name='reading_lists'
    )  # Usuario propietario de la lista
    name = models.CharField(max_length=100)  # Nombre de la lista
    description = models.TextField(blank=True, null=True)  # Descripción de la lista
    books = models.ManyToManyField(Book, related_name='in_reading_lists')  # Libros en la lista
    is_public = models.BooleanField(default=False)  # Si la lista es pública o privada
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación

    def __str__(self):
        return f"{self.name} by {self.user.username}"


# Modelo para reseñas de libros
class BookReview(models.Model):
    """Modelo para reseñas de libros por los usuarios"""
    user = models.ForeignKey(
        LibraryUser, on_delete=models.CASCADE, related_name='reviews'
    )  # Usuario que deja la reseña
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='reviews'
    )  # Libro reseñado
    rating = models.PositiveSmallIntegerField(
        choices=[(i, i) for i in range(1, 6)]
    )  # Calificación (1 a 5 estrellas)
    comment = models.TextField()  # Comentario de la reseña
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación

    class Meta:
        unique_together = ('user', 'book')  # Un usuario solo puede reseñar un libro una vez

    def __str__(self):
        return f"Review of {self.book.title} by {self.user.username}"