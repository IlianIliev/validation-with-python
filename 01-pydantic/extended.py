from typing import Optional

from base import User


class BusinessUser(User):
    company_name: str
    vat_id: Optional[str]


business_user = BusinessUser(
    id=1, email="company@example.org", company_name="Example Inc."
)
print("Business user:", business_user.json(indent=4))
