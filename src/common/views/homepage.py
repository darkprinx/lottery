from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class HomePageView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "homepage.html"

    def get(self, request):
        ctx = {
            "header": "Welcome to Fake Lottery",
            "subheader": "Your gateway to exciting lottery experiences! "
            "Simple, powerful, and designed for you.",
            "primary_cta_text": "Admin Login",
            "primary_cta_link": "/admin/",
            "secondary_cta_text": "Learn More",
            "secondary_cta_link": "/redoc/",
        }
        return Response(ctx)
