from unittest import mock
from django.test import TestCase
from common.helpers.random_number_generator_helper import generate_customized_uuid


class TestRandomNumberGenerator(TestCase):

    @mock.patch('uuid.uuid4')
    def test_generate_customized_uuid_with_prefix(self, mock_uuid):
        expected = '1-3d84jx83ks9ss98lk92jasrcmsis93'
        mock_uuid.return_value = '3d84jx83ks9ss98lk92jasrcmsis93'

        actual = generate_customized_uuid('1')
        self.assertEqual(expected, actual)

    @mock.patch('uuid.uuid4')
    def test_generate_customized_uuid_without_prefix(self, mock_uuid):
        expected = '3d84jx83ks9ss98lk92jasrcmsis93'
        mock_uuid.return_value = expected

        actual = generate_customized_uuid()
        self.assertEqual(expected, actual)

    def test_generate_customized_uuid_mismatch(self):
        expected = '3d84jx83ks9ss98lk92jasrcmsis93'
        actual = generate_customized_uuid()
        self.assertNotEqual(expected, actual)
