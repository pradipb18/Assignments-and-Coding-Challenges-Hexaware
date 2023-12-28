class InvalidDataException(Exception):
    def __init__(self, message="Invalid data entered"):
        self.message = message
        super().__init__(self.message)

class InsufficientStockException(Exception):
    def __init__(self, message="Insufficient stock to fulfill the order"):
        self.message = message
        super().__init__(self.message)

class IncompleteOrderException(Exception):
    def __init__(self, message="Incomplete order details. Product reference missing"):
        self.message = message
        super().__init__(self.message)

class PaymentFailedException(Exception):
    def __init__(self, message="Payment for the order has failed"):
        self.message = message
        super().__init__(self.message)
class PaymentProcessingException(Exception):
    def __init__(self, message="Payment processing failed"):
        self.message = message
        super().__init__(self.message)
class FileIOException(Exception):
    def __init__(self, message="Error during file I/O"):
        self.message = message
        super().__init__(self.message)

class DatabaseConnectionException(Exception):
    def __init__(self, message="Unable to connect to the database"):
        self.message = message
        super().__init__(self.message)

class ConcurrencyException(Exception):
    def __init__(self, message="Concurrency issue. Please retry your operation"):
        self.message = message
        super().__init__(self.message)

class AuthenticationException(Exception):
    def __init__(self, message="Authentication failed"):
        self.message = message
        super().__init__(self.message)

class AuthorizationException(Exception):
    def __init__(self, message="Unauthorized access"):
        self.message = message
        super().__init__(self.message)