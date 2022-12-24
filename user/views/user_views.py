from rest_framework import viewsets
from django.contrib.auth.models import User

from user.serializers.user_serializers import UserSerializer


class UserView(viewsets.ModelViewSet):
    """
    ## This view contains a set of all the basic CRUD operation endpoints related to User entity.
    ## user can get list, create, update, delete User entity to the system via these endpoints.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
