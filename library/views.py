from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from .models import Book
from .forms import BookForm

from .filters import BookFilter
from config.settings import redis_instance
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from .mixins import AuthorRequiredMixin


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "library/register.html"
    success_url = reverse_lazy("login")


class BookListView(FilterView):
    model = Book
    template_name = "library/book_list.html"
    context_object_name = "books"
    filterset_class = BookFilter
    paginate_by = 10


class BookDetailView(DetailView):
    model = Book
    template_name = "library/book_detail.html"
    context_object_name = "book"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        # Increasing number of views per object in Redis
        redis_instance.incr(f"book:{self.object.id}:views")

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    login_url = "library:login"
    template_name = "library/book_form.html"
    success_url = reverse_lazy("library:book_list")

    def form_valid(self, form):
        form.instance.user_author = self.request.user
        response = super().form_valid(form)
        return response


class BookUpdateView(LoginRequiredMixin, AuthorRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = "library/book_form.html"
    success_url = reverse_lazy("library:book_list")


class BookDeleteView(LoginRequiredMixin, AuthorRequiredMixin, DeleteView):
    model = Book
    template_name = "library/book_confirm_delete.html"
    success_url = reverse_lazy("library:book_list")
