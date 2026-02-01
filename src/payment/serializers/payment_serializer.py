from rest_framework import serializers

from payment.models import TransactionHistory


class TransactionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionHistory
        fields = (
            "paid_by",
            "amount",
            "payment_via",
            "description",
            "transaction_id",
            "status",
        )
