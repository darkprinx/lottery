import logging

from rest_framework import generics
from rest_framework.response import Response

from utils.helpers.payment_helper import PaymentFactory
from payment.models import TransactionHistory
from payment.serializers.payment_serializer import TransactionHistorySerializer

logger = logging.getLogger(__name__)


class MakePaymentView(generics.CreateAPIView):
    serializer_class = TransactionHistorySerializer
    queryset = TransactionHistory.objects.all()

    def post(self, request):
        """
        ## Use this endpoint to make payment before purchasing a ballot.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        payment_service = PaymentFactory().get_payment_service(
            serializer.data["payment_via"]
        )
        response = payment_service.make_payment(serializer.data)

        request.data.update(response)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)
