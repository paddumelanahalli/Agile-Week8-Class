#test_email.py
import pytest
from email_tools import get_valid_emails

def test_get_valid_emails():
    input_list = ["nathan@ucsc.edu", "invalid-email", "aruna@work.com"]
    expected = ["nathan@ucsc.edu", "aruna@work.com"]

def test_handle_non_string_data():
    # This list has an integer and a None. It SHOULD just ignore them.
    input_data = ["nathan@ucsc.edu", 12345, None]
    expected = ["nathan@ucsc.edu"]

    assert get_valid_emails(input_data) == expected

#email_tools.py
"""

\def get_valid_emails(emails):
    return [e for e in emails if "@" in e]
"""

def get_valid_emails(emails):
    # Refactor: Ensure it's a string AND has the @ symbol
    return [
        e for e in emails
        if isinstance(e, str) and "@" in e
    ]
