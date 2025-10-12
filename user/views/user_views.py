from rest_framework import viewsets
from django.contrib.auth.models import User

from user.serializers.user_serializers import UserSerializer


class UserView(viewsets.ModelViewSet):
    """
    ## CRUD endpoints for the User entity:
    ## list, create, update, and delete.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
