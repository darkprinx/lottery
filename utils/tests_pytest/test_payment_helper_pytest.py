import uuid

import pytest
from rest_framework.serializers import ValidationError

from utils.helpers.payment_helper import (
    MobilePaymentService,
    CardPaymentService,
    PaymentFactory,
)


class DummyUUID:
    def __init__(self, hex_value: str):
        self.hex = hex_value


def test_mobile_payment_service_returns_expected_payload(monkeypatch):
    monkeypatch.setattr(uuid, "uuid4", lambda: DummyUUID("fixed-hex-123"))
    service = MobilePaymentService()

    result = service.make_payment()

    assert result == {
        "payment_via": "mobile_payment",
        "transaction_id": "fixed-hex-123",
        "status": "successful",
    }


def test_card_payment_service_returns_expected_payload(monkeypatch):
    monkeypatch.setattr(uuid, "uuid4", lambda: DummyUUID("card-hex-456"))
    service = CardPaymentService()

    result = service.make_payment()

    assert result == {
        "payment_via": "card_payment",
        "transaction_id": "card-hex-456",
        "status": "successful",
    }


def test_payment_factory_returns_correct_service_instances():
    factory = PaymentFactory()

    mobile = factory.get_payment_service("mobile_payment")
    card = factory.get_payment_service("card_payment")

    assert isinstance(mobile, MobilePaymentService)
    assert isinstance(card, CardPaymentService)


def test_payment_factory_raises_for_unsupported_service():
    factory = PaymentFactory()

    with pytest.raises(ValidationError) as exc:
        factory.get_payment_service("crypto_payment")

    # Ensure the error message mentions available services
    msg = str(exc.value)
    assert "not implemented or attached to the system" in msg
    assert "mobile_payment" in msg and "card_payment" in msg
