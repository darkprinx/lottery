from unittest import mock
from django.test import TestCase

from utils.helpers.payment_helper import MobilePaymentService


class TestMobilePaymentService(TestCase):
    def setUp(self) -> None:
        self.payment_service = MobilePaymentService()
        self.payment_via = "mobile_payment"

    @mock.patch("uuid.uuid4")
    def test_make_payment(self, mock_uuid):
        mock_uuid.return_value.hex = "3d84jx83ks9ss98lk92jasrcmsis93"
        expected = {
            "payment_via": self.payment_via,
            "transaction_id": mock_uuid.return_value.hex,
            "status": "successful",
        }

        actual = self.payment_service.make_payment()
        self.assertEqual(expected, actual)
