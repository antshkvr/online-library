from django.core.exceptions import PermissionDenied


class AuthorRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user_author != request.user:
            raise PermissionDenied("You are not an author of this book")
        return super().dispatch(request, *args, **kwargs)
