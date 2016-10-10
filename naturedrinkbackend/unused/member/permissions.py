from rest_framework import permissions
from django.contrib.auth.models import User

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
