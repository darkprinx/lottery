from rest_framework import viewsets
from django.contrib.auth.models import User

from user.serializers.user_serializers import UserSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
