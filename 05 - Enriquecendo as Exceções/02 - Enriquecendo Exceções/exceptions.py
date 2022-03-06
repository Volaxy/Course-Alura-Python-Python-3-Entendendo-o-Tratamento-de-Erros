class InsufficientFundsException(Exception):
    # To allow multiple parameters in the call of this function, put the "*args" or/and "**kwargs" in the signature
    def __init__(self, message="", balance=None, value=None, *args):
        self.balance = balance
        self.value = value

        msg = "Insufficient balance to carry out the transaction" \
              f"Current balance: {self.balance} Amount to be withdrawn: {self.value}"

        # To execute the constructor of our class, the "super()" is used
        # Case the "message" is Null, the "msg" will be passed as a parameter
        super(InsufficientFundsException, self).__init__(message or msg, *args)
