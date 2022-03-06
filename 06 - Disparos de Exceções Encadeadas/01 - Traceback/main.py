from exceptions import InsufficientFundsException


class Client:
    def __init__(self, name, cpf, profession):
        self.name = name
        self.cpf = cpf
        self.profession = profession

    def __str__(self):
        return f"Name: {self.name}, CPF: {self.cpf}, Profession: {self.profession}"


class CheckingAccount:
    total_accounts_created = 0
    operation_tax = None

    def __init__(self, client, agency, number):
        self.__balance = 100
        self.client = client
        self.__agency = agency
        self.__number = number

        CheckingAccount.total_accounts_created += 1
        CheckingAccount.operation_tax = 30 / CheckingAccount.total_accounts_created

    def transfer(self, value, favored):
        if value < 0:
            raise ValueError("The amount to be withdrawn cannot be less than 0")
        if value > self.__balance:
            raise InsufficientFundsException("", self.balance, value)

        self.withdraw(value)
        favored.deposit(value)

    def withdraw(self, value):
        if value < 0:
            raise ValueError("The amount to be withdrawn cannot be less than 0")
        if value > self.__balance:
            raise InsufficientFundsException("", self.balance, value)

        self.__balance -= value

    def deposit(self, value):
        self.__balance += value

    @property
    def agency(self):
        return self.__agency

    def __set_agency(self, agency):
        if not isinstance(agency, int):
            raise ValueError("The attribute must be an integer")
        if agency <= 0:
            raise ValueError("The agency must be grater than 0")

        self.__agency = agency

    @property
    def number(self):
        return self.__number

    def __set_number(self, number):
        if not isinstance(number, int):
            raise ValueError("The attribute must be an integer")
        if number <= 0:
            raise ValueError("The number must be grater than 0")

        self.__number = number

    @property
    def balance(self):
        return self.__balance

    def __set_balance(self, balance):
        if not isinstance(balance, int):
            raise ValueError("The attribute must be an integer")
        if balance <= 0:
            raise ValueError("The balance must be grater than 0")

        self.__balance = balance


def __main__():
    try:
        account1 = CheckingAccount(None, 1, 1)
        account2 = CheckingAccount(None, 2, 2)

        print(account1.balance)
        print(account2.balance)
        print()

        account1.transfer(1000, account2)

        print(account1.balance)
        print(account2.balance)
    except InsufficientFundsException as e:
        import traceback

        print(e.balance)
        print(e.value)
        print("Exception type:", e.__class__.__name__)

        # To print the traceback of the exception, just use the "traceback.print_exc()" to view the stack of call method
        traceback.print_exc()


if __name__ == "__main__":
    __main__()
