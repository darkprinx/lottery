from rest_framework import serializers

from payment.models import TransactionHistory
from user.serializers.user_serializers import UserNameEmailSerializer


class TransactionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionHistory
        fields = ('paid_by', 'amount', 'payment_via', 'description', 'transaction_id', 'status')
