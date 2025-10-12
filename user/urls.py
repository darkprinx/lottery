from rest_framework import routers
from user.views.user_views import UserView

user_router = routers.DefaultRouter()
user_router.register("", UserView)

urlpatterns = [] + user_router.urls
