"""Validation utilities for country codes, phone numbers, and capabilities."""
import re
from typing import Optional, Iterable

from .country_data import COUNTRY_DATA, get_area_codes, get_country_code

# Allowed capability types
ALLOWED_CAPABILITIES = {'voice', 'sms', 'mms'}


def is_valid_country_iso(country_iso: str) -> bool:
    """
    Check if the given country ISO code is supported.
    """
    if not isinstance(country_iso, str):
        return False
    return country_iso.upper() in COUNTRY_DATA


def is_valid_phone_number_format(number: str, country_iso: Optional[str] = None) -> bool:
    """
    Validate phone number format (E.164) and optional country-specific area code.

    - Must match E.164: '+' followed by 1-15 digits, first digit non-zero.
    - If country_iso provided, number must start with its dialing prefix,
      and the next digits must match a known area code if available.
    """
    if not isinstance(number, str):
        return False
    # E.164 pattern: '+' followed by 1-15 digits, first digit 1-9
    if not re.fullmatch(r"\+[1-9]\d{1,14}", number):
        return False

    if country_iso:
        cc = get_country_code(country_iso)
        if not cc:
            return False
        if not number.startswith(f'+{cc}'):
            return False
        # Remove country code prefix
        rest = number[len(cc) + 1:]
        # Validate area code if dataset contains area codes
        area_codes = get_area_codes(country_iso)
        if area_codes:
            for ac in area_codes:
                ac_str = str(ac)
                if rest.startswith(ac_str):
                    return True
            return False
    return True


def is_valid_capabilities(capabilities: Iterable[str]) -> bool:
    """
    Validate that each capability is one of the allowed types.
    """
    try:
        caps = {cap.lower() for cap in capabilities}
    except Exception:
        return False
    return caps.issubset(ALLOWED_CAPABILITIES)