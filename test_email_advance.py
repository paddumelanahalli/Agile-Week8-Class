#test_email_advance.py
import pytest
from email_tools import get_valid_emails

# We define the input list and the expected result as a "data table"
@pytest.mark.parametrize("input_list, expected_output", [
    (["valid@ucsc.edu"], ["valid@ucsc.edu"]),             # Standard case
    (["no_at_sign", "ok@me.com"], ["ok@me.com"]),         # Mix case
    ([], []),                                             # Empty case
    ([123, None, "test@test.com"], ["test@test.com"]),    # Dirty data case
])
def test_email_filtering_at_scale(input_list, expected_output):
    # This single line now runs 4 different tests!
    assert get_valid_emails(input_list) == expected_output
