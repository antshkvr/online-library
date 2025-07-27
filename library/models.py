from django.db import models
from django.contrib.auth import get_user_model


class Book(models.Model):
    GENRE_CHOICES = [
        ("fiction", "Fiction"),
        ("nonfiction", "Non-Fiction"),
        ("fantasy", "Fantasy"),
        ("sci-fi", "Sci-Fi"),
        ("romance", "Romance"),
        ("horror", "Horror"),
        ("other", "Other"),
    ]

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    file = models.FileField(upload_to="books/")
    description = models.TextField(blank=True)
    download_count = models.PositiveIntegerField(default=0)
    user_author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="books"
    )

    def __str__(self):
        return self.title
