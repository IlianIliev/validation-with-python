from django import forms


class UserForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    age = forms.IntegerField(required=False)


class BusinessUserForm(UserForm):
    company = forms.CharField(max_length=100)
    country = forms.CharField(max_length=2)
    vat_id = forms.CharField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        country = cleaned_data.get("country")
        vat_id = cleaned_data.get("vat_id")

        if all([country, vat_id]) and not vat_id.startswith(country):
            raise forms.ValidationError(
                {"vat_id": f"VAT ID must start with country code {country}."}
            )

        return cleaned_data
