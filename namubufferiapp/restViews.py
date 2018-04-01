from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework import routers
from rest_framework import permissions


from .serializers import UserTagSerializer
from .models import UserTag


class HasPermissionForNamubufferiObject(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            try:
                requestUser = User.objects.get(id=int(request.data["user"]))
                if requestUser == request.user:
                    return True
            except KeyError:
                return True

        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            try:
                if obj.user == request.user:
                    return True
            except AttributeError:
                return False
        else:
            try:
                requestUser = User.objects.get(id=int(request.data["user"]))
                if requestUser == request.user:
                    return True
            except KeyError:
                return False

        return False

class NamubufferiModelViewSet(viewsets.ModelViewSet):
    namubufferiObject = None
    serializer_class = None

    permission_classes = (HasPermissionForNamubufferiObject,)

    def get_queryset(self):
        return self.namubufferiObject.objects.filter(user=self.request.user)


class UserTagViewSet(NamubufferiModelViewSet):
    """
    API endpoint that allows user tags to be viewed or edited.
    """
    namubufferiObject = UserTag
    serializer_class = UserTagSerializer



router = routers.DefaultRouter()
router.register(r'userTags', UserTagViewSet, base_name="userTags")
