from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    """
    Read allowed for anyone; write allowed only if obj.author == request.user.username.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        username = getattr(request.user, "username", None)
        return getattr(obj, "author", None) == username

