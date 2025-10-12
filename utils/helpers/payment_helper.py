import uuid
from abc import ABC, abstractmethod
from rest_framework.serializers import ValidationError


class BasePaymentService(ABC):
    @abstractmethod
    def make_payment(self, *args, **kwargs):
        pass


"""
Assumes attachment to a real payment service.
For simplicity, only an abstract base and a dummy concrete class
are implemented with placeholder methods.
"""


class MobilePaymentService:
    def __init__(self):
        pass

    def make_payment(self, *args, **kwargs):
        print("Payment made via mobile payment service")
        return {
            "payment_via": "mobile_payment",
            "transaction_id": uuid.uuid4().hex,
            "status": "successful",
        }


class CardPaymentService:
    def __init__(self):
        pass

    def make_payment(self, *args, **kwargs):
        print("Payment made via card payment service")
        return {
            "payment_via": "card_payment",
            "transaction_id": uuid.uuid4().hex,
            "status": "successful",
        }


class PaymentFactory:
    payment_services = {
        "mobile_payment": MobilePaymentService(),
        "card_payment": CardPaymentService(),
    }

    def get_payment_service(self, payment_service_type):
        if payment_service_type not in self.payment_services:
            raise ValidationError(
                {
                    "payment_via": (
                        f"{payment_service_type} is not implemented or attached to the "
                        f"system. Available services are "
                        f"{list(self.payment_services.keys())}"
                    )
                }
            )
        return self.payment_services[payment_service_type]
