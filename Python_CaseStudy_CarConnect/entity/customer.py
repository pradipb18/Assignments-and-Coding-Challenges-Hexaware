
class Customer:
    def __init__(self, customer_id, first_name, last_name, email, phone_number, address, username, password, registration_date):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.username = username
        self.password = password
        self.registration_date = registration_date

    def authenticate(self, password):
        if password == self.password:
            return True
        else:
            return False


