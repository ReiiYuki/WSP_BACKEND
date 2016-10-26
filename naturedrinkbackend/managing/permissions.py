from rest_framework import permissions

class isAdmin(permissions.BasePermission) :
    def has_permission(self, request, view):
        return request.user.is_staff
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff
