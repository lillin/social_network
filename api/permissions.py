from rest_framework import permissions


class ModifyOnlyOwner(permissions.BasePermission):
    message = 'Only owners can update or delete their posts.'

    def has_object_permission(self, request, view, obj):
        if request.method in ('PUT', 'PATCH', 'DELETE'):
            return obj.creator == request.user
        return True
