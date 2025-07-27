from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)
from django.contrib.auth import views as auth_views
from .views import RegisterView


app_name = "library"

urlpatterns = [
    path("", BookListView.as_view(), name="book_list"),
    path("<int:pk>/", BookDetailView.as_view(), name="book_detail"),
    path("add/", BookCreateView.as_view(), name="book_create"),
]

urlpatterns += [
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="registration/logout.html"),
        name="logout",
    ),
    path("register/", RegisterView.as_view(), name="register"),
]

urlpatterns += [
    path("books/<int:pk>/edit/", BookUpdateView.as_view(), name="book_edit"),
    path("books/<int:pk>/delete/", BookDeleteView.as_view(), name="book_delete"),
]
