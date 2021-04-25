from rest_framework import permissions
from rest_framework.permissions import BasePermission


# Custom permission for users with "is_active" = True.
class IsArtistT(BasePermission):
    """
    Allows access only to "is_active" users.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:

            return True
        else:
            print('here now')
            if request.user.is_reader == False:
                return True
            else:
                return False

class IsArtist(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:

            return True
        else:
            print('here now')
            if request.user.is_artist:
                return True
            else:
                return False



        # Instance must have an attribute named `owner`.
