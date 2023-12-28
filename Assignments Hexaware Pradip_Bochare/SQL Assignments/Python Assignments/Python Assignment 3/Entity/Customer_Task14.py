import re
class Customer:
    def __init__(self, customer_id="", first_name="", last_name="", email="", phone_number="", address=""):
        self._CustomerID = customer_id
        self._FirstName = first_name
        self._LastName = last_name
        self._Email = email
        self._PhoneNumber = phone_number
        self._Address = address

    @property
    def CustomerID(self):
        return self._CustomerID

    @CustomerID.setter
    def CustomerID(self, new_customer_id):
        if isinstance(new_customer_id, str) and new_customer_id:
            self._CustomerID = new_customer_id
        else:
            raise ValueError("Customer ID must be a non-empty string.")

    @property
    def FirstName(self):
        return self._FirstName

    @FirstName.setter
    def FirstName(self, new_first_name):
        if isinstance(new_first_name, str) and new_first_name:
            self._FirstName = new_first_name
        else:
            raise ValueError("First Name must be a non-empty string.")

    @property
    def LastName(self):
        return self._LastName

    @LastName.setter
    def LastName(self, new_last_name):
        if isinstance(new_last_name, str) and new_last_name:
            self._LastName = new_last_name
        else:
            raise ValueError("Last Name must be a non-empty string.")

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, new_email):
        if isinstance(new_email, str) and re.match(r"[^@]+@[^@]+\.[^@]+", new_email):
            self._Email = new_email
        else:
            raise ValueError("Invalid Email format.")

    @property
    def PhoneNumber(self):
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, new_phone_number):
        if isinstance(new_phone_number, str) and re.match(r"\d{10}", new_phone_number):
            self._PhoneNumber = new_phone_number
        else:
            raise ValueError("Invalid phone number format.")

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, new_address):
        if isinstance(new_address, str) and new_address:
            self._Address = new_address
        else:
            raise ValueError("Address must be a non-empty string.")