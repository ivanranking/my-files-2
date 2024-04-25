def find_phone_number(phone_book, name):
    """
    Find a phone number in the phone book.

    Args:
    phone_book (dict): A dictionary containing names as keys and phone numbers as values.
    name (str): The name to search for in the phone book.

    Returns:
    str: The phone number corresponding to the given name, or 'Phone number not found' if the name is not in the phone book.
    """
    if name in phone_book:
        return phone_book[name]
    else:
        return 'Phone number not found'

# Example phone book
phone_book = {
    'Alice': '555-1234',
    'Bob': '555-5678',
    'Charlie': '555-9999'
}

# Search for a phone number
name_to_find = 'Bob'
result = find_phone_number(phone_book, name_to_find)
print(f"The phone number for {name_to_find} is: {result}")
