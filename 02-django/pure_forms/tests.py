from django.test import TestCase

from pure_forms.forms import UserForm


class TestUserForm(TestCase):
    def test_empty_forms(self):  # Empty form
        # Empty forms are not valid, but has no errors
        form = UserForm()

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {})

    def test_invalid_data(self):
        form = UserForm({"name": "John", "email": ""})

        # Form with invalid data has errors
        self.assertFalse(form.is_valid())

        # Errors are objects
        self.assertEqual(form.errors, {"email": ["This field is required."]})

        # Errors are represented as HTML
        self.assertEqual(
            str(form.errors),
            '<ul class="errorlist"><li>email<ul class="errorlist"><li>This field is required.</li></ul></li></ul>',  # noqa: E501
        )

    def test_valid_data(self):
        form = UserForm({"name": "John", "email": "john@example.org"})
        self.assertTrue(form.is_valid())

        self.assertEqual(
            form.cleaned_data,
            {"name": "John", "email": "john@example.org", "age": None},
        )
