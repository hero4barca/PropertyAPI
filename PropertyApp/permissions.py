from rest_framework import permissions

class IsOwnerOrReadOnly (permissions.BasePermission):
    """
    Custom permission only allows owner of code snippet to edit or delete it
    """
    def has_object_permission(self, request, view, obj):
        #read permission allowed for every request
        # always allow GET, HEAD or OPTIONS request
        if request.method in permissions.SAFE_METHODS:
            return True
        

        #allow other methods if user is the owner of the snippet
        return obj.agent == request.user
            