from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    ALLOWED_CONTENT_TYPES = [
        "application/pdf",
        "application/epub+zip",
    ]

    class Meta:
        model = Book
        fields = ["title", "author", "genre", "description", "file"]

    def clean_file(self):
        file = self.cleaned_data.get("file")
        if file:
            content_type = getattr(
                file, "content_type", None
            )  # When editing existing book content_type of file is None
            if not content_type:
                pass
            else:
                if content_type not in self.ALLOWED_CONTENT_TYPES:
                    raise forms.ValidationError("Can process only PDF and Epub files")
                if file.size > 100 * 1024 * 1024:  # Limit for books is 100 MB
                    raise forms.ValidationError("File size cannot exceed 100 MB")
        return file
