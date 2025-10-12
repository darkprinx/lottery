from rest_framework import permissions
from django.conf import settings


class IsValidRequest(permissions.BasePermission):
    """
    Global permission check for blocked IPs.
    """

    def has_permission(self, request, view):
        authorization_token = request.headers.get("Authorization")
        if authorization_token:
            authorization_token = authorization_token.replace("Bearer", "")
        return authorization_token == settings.CUSTOM_API_TOKEN
