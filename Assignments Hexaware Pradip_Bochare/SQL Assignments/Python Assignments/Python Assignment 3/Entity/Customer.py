
class Customer:
    def __init__(self, CustomerID, FirstName, LastName, Email, PhoneNumber, Address):
        self._CustomerID = CustomerID
        self._FirstName = FirstName
        self._LastName= LastName
        self._Email = Email
        self._PhoneNumber = PhoneNumber
        self._Address = Address
    @property
    def CustomerID(self):
        return self._CustomerID

    @CustomerID.setter
    def CustomerID(self, new_CustomerID):
        if isinstance(new_CustomerID, str) and new_CustomerID:
            self._CustomerID = new_CustomerID
        else:
            raise ValueError("Customer ID must be a non-empty string.")
    @property
    def FirstName(self):
        return self._FirstName

    @FirstName.setter
    def FirstName(self, new_FirstName):
        if isinstance(new_FirstName, str) and new_FirstName:
            self._FirstName = new_FirstName
        else:
            raise ValueError("First Name must be a non-empty string.")

    @property
    def LastName(self):
        return self._LastName

    @LastName.setter
    def LastName(self, new_LastName):
        if isinstance(new_LastName, str) and new_LastName:
            self._LastName= new_LastName
        else:
            raise ValueError("Last Name must be a non-empty string.")

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, new_Email):
        if isinstance(new_Email, str) and "@" in new_Email:
            self._Email = new_Email
        else:
            raise ValueError("Invalid Email format.")

    @property
    def PhoneNumber(self):
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, new_PhoneNumber):
        if isinstance(new_PhoneNumber, str) and new_PhoneNumber.isdigit():
            self._PhoneNumber = new_PhoneNumber
        else:
            raise ValueError("Invalid phone number format.")

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, new_Address):
        if isinstance(new_Address, str) and new_Address:
            self._Address = new_Address
        else:
            raise ValueError("Address must be a non-empty string.")



