from dataclasses import dataclass

@dataclass
class PhoneNumberModel:
    phone_number: str
    country_code: str
    region: str
    type: str
    price: float
