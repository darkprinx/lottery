from model_bakery import baker
from django.test import TestCase, RequestFactory
from lottery_event.models import LotteryEvent
from django.contrib.auth import get_user_model
from django.urls import reverse

from lottery_event.views.lottery_event_views import RegisterLotteryView


class TestRegisterLotteryView(TestCase):

    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.user = baker.make(get_user_model(), id=1)
        self.lottery_event_object = baker.make(LotteryEvent, id=1)
        self.request_url = reverse('register-lottery')

    def test_successful_registration_200(self):
        data = {
            "user_id": 1,
            "lottery_event_id": 1
        }

        request = self.factory.post(self.request_url, data)
        response = RegisterLotteryView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_validation_error_400(self):
        data = {
            "user_id": 2,
            "lottery_event_id": 2
        }

        request = self.factory.post(self.request_url, data)
        response = RegisterLotteryView.as_view()(request)
        self.assertEqual(response.status_code, 400)
