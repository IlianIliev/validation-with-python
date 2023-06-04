from django.test import TestCase

from model_forms.forms import UserForm
from model_forms.models import User


# Create your tests here.
class ModelFormTest(TestCase):
    def test_empty_form(self):
        form = UserForm()
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {})

    def test_invalid_form(self):
        form = UserForm({"name": "John", "email": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors,
            {"email": ["This field is required."]},
        )

    def test_valid_form(self):
        self.assertFalse(User.objects.filter(name="John").exists())

        form = UserForm({"name": "John", "email": "john@example.org"})
        self.assertTrue(form.is_valid())

        self.assertEqual(
            form.cleaned_data,
            {"name": "John", "email": "john@example.org", "age": None},
        )

        form.save()

        self.assertTrue(User.objects.filter(name="John").exists())
