from django.test import TestCase

from api.serialisers import UserSerializer
from model_forms.models import User


class TestSerializer(TestCase):
    def test_empty_serializer(self):
        serializer = UserSerializer()

        # You can not call is_valid() without providing any data
        self.assertRaises(AssertionError, serializer.is_valid)

        serializer = UserSerializer(data={})
        self.assertFalse(serializer.is_valid())

    def test_invalid_serializer(self):
        serializer = UserSerializer(data={"name": "John", "email": ""})
        self.assertFalse(serializer.is_valid())

        self.assertEqual(
            serializer.errors,
            {"email": ["This field may not be blank."]},
        )

    def test_valid_serializer(self):
        self.assertFalse(User.objects.filter(name="John").exists())

        serializer = UserSerializer(data={"name": "John", "email": "john@example.org"})
        self.assertTrue(serializer.is_valid())

        serializer.save()

        self.assertTrue(User.objects.filter(name="John").exists())
