from rest_framework import generics
from rest_framework.response import Response

from common.helpers.payment_helper import PaymentFactory
from payment.serializers.payment_serializer import TransactionHistorySerializer


class MakePaymentView(generics.CreateAPIView):
    serializer_class = TransactionHistorySerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        payment_service = PaymentFactory().get_payment_service(serializer.data['payment_via'])
        response = payment_service.make_payment(serializer.data)

        request.data.update(response)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)


