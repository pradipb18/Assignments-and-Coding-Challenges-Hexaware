class InsufficientFundException(Exception):
    def __init__(self, message="Insufficient funds."):
        self.message = message
        super().__init__(self.message)

class InvalidAccountException(Exception):
    def __init__(self, message="Invalid account number."):
        self.message = message
        super().__init__(self.message)

class OverDraftLimitExceededException(Exception):
    def __init__(self, message="Overdraft limit exceeded."):
        self.message = message
        super().__init__(self.message)