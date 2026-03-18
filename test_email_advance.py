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

#Refractor method - in the real world checking isinstance and in inside a list 
#comprehension is fine for 10 emails but what about 10 million?
# We can refractor to use Generator Expression for better memory efficiency

def get_valid_emails(emails):
    """ 
    Refractored to handle potential memory leaks by using
    a generator for massive database 
    """
    if not isinstance(emails,list):
        raise TypeError("Input must be a list of strings")
    """
    using a generator ensures we don't build the whole list
    in memory if we are just iterating over it later
    """
    valid_generator = (e for e in emails if isinstance(e,str) and "@" in e)
    return list(valid_generator)
