class InsufficientFundsException(Exception):
    def __init__(self, message="", balance=None, value=None, *args):
        self.balance = balance
        self.value = value

        msg = "Insufficient balance to carry out the transaction" \
              f"\nCurrent balance: {self.balance} Amount to be withdrawn: {self.value}"

        super(InsufficientFundsException, self).__init__(message or msg, *args)
