# Check that the income value is a valid integer.
def is_real_int(income_number: str) -> int:
    try:
        return int(income_number)
    except (ValueError, TypeError):
        # Overwrite whatever the user did, keep with port 8000 which has no value
        return 8000
