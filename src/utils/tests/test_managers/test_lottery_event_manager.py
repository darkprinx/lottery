from django.test import TestCase
from model_bakery import baker

from event.models import Event
from utils.managers.lottery_event_manager import EventManager


class TestEventManager(TestCase):
    def setUp(self) -> None:
        self.lottery_event1 = baker.make(Event, id=1, status="active")
        self.lottery_event_manager = EventManager()

    def test_get_lottery_event_by_id(self):
        actual = self.lottery_event_manager.get_lottery_event_by_id(lottery_event_id=1)
        expected = self.lottery_event1
        self.assertEqual(actual, expected)

    def test_get_lottery_event_by_id_not_exists(self):
        actual = self.lottery_event_manager.get_lottery_event_by_id(lottery_event_id=3)
        expected = None
        self.assertEqual(actual, expected)

    def test_is_active_lottery_event(self):
        actual = self.lottery_event_manager.is_active_lottery_event(lottery_event_id=1)
        expected = self.lottery_event1.status == "active"
        self.assertEqual(actual, expected)
