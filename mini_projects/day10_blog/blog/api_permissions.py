from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    """
    SAFE methods allowed to anyone.
    Write methods allowed only if the object's 'author' matches request.user.username.
    Note: Your Post/Comment 'author' is a CharField, not FK, so we compare strings.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        user = getattr(request, "user", None)
        if not user or not user.is_authenticated:
            return False
        # obj may be Post or Comment
        if hasattr(obj, "author"):
            return obj.author == user.username
        # fallback deny
        return False

