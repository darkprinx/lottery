import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from common.custom_permissions.custom_authentication_permission import IsValidRequest

logger = logging.getLogger(__name__)


class HelloView(APIView):

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
