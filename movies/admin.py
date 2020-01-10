from django.contrib import admin
from .models import  Category, Genre, Movie, MovieShots, Actor, Rating, RatingStar, Reviews
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Категории"""
    list_display = ('id', 'name', 'url')
    list_display_links = ("name",)


class ReviewsInline(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ('name', 'email')



@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """Фильм"""
    list_display = ('title', 'category', 'url', 'draft')
    list_filter = ('category', 'year')
    search_fields = ('title', 'category__name',)
    inlines = [ReviewsInline]
    save_on_top = True
    save_as = True
    list_editable = ('draft',)

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    """Отзывы"""
    list_display = ( 'name', 'email', 'text', 'parent', 'movie', 'id' )
    readonly_fields = ('name', 'email',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Жанры"""
    list_display = ('name', 'description', 'url', )

@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    """Кадры из фильма"""
    list_display = ('title', 'description', 'image', 'movie', )

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    """Актеры и режиссеры"""
    list_display = ('name', 'age', 'description', 'image', )

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Рейтинг"""
    list_display = ('ip', 'star', 'movie', )

@admin.register(RatingStar)
class RatingStarAdmin(admin.ModelAdmin):
    """Звезда рейтинга"""
    list_display = ('value', )






