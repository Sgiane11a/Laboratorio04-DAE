from django.contrib import admin
from .models import BookView, CategoryAnalytics, AuthorAnalytics, RecommendationLog

@admin.register(BookView)
class BookViewAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'timestamp')

@admin.register(CategoryAnalytics)
class CategoryAnalyticsAdmin(admin.ModelAdmin):
    list_display = ('category', 'total_views', 'total_books', 'popularity_score')

@admin.register(AuthorAnalytics)
class AuthorAnalyticsAdmin(admin.ModelAdmin):
    list_display = ('author', 'total_views', 'avg_rating', 'total_reviews')

@admin.register(RecommendationLog)
class RecommendationLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'reason', 'clicked', 'timestamp')