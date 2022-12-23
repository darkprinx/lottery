from django.urls import path

from payment.views.payment_views import MakePaymentView

urlpatterns = [
    path('make-payment/', MakePaymentView.as_view(), name='make-payment'),
]
