import re

def is_valid_email(email):
    # Regular expression for validating an email
    email_regex = re.compile(
        r"^(?=.{1,256})(?=.{1,64}@.{1,255})[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+"
        r"(?:\.[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,63}$"
    )
    return re.match(email_regex, email) is not None