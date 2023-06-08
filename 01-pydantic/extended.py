from typing import Optional

from pydantic import validator, root_validator

from base import User


# Pydantic models are easy to extend
class BusinessUser(User):
    company_name: str
    country: str
    vat_id: Optional[str]

    @validator("country")
    @classmethod
    def validate_country(cls, country):
        if len(country) != 2:
            raise ValueError("Country must be a two-letter code.")
        return country

    @root_validator()
    def validate_country_and_vat_id(cls, values):
        country = values.get("country")
        vat_id = values.get("vat_id")

        if all([country, vat_id]) and not vat_id.startswith(country):
            raise ValueError(f"VAT ID must start with country code {country}.")

        return values
