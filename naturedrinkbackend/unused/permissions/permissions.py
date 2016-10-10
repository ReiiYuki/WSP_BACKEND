from rest_framework import permissions

class IsOwnerOrIsAdmin(permissions.BasePermission):
    def has_permission(self, request, view) :
        return not request.user.is_anonymous
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_superuser


class AuthorizedOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view) :
        if request.method == 'POST' :
            return True
        return not request.user.is_anonymous
    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_superuser

class AdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST' :
            return request.user.is_superuser
        return True
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_superuser
