import django_filters
from .models import Book


class BookFilter(django_filters.FilterSet):
    author = django_filters.CharFilter(lookup_expr="icontains", label="Автор")
    genre = django_filters.ChoiceFilter(choices=Book.GENRE_CHOICES, label="Жанр")

    class Meta:
        model = Book
        fields = ["author", "genre"]
