from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Правило доступа, разрешающее изменение объекта только его автору,
    в то время как чтение доступно всем."""
    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user == obj.author
        )
