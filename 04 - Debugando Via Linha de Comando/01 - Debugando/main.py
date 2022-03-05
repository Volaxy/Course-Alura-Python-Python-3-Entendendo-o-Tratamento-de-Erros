import sys


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
        favored.deposit(value)

    def withdraw(self, value):
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
    accounts = []
    while True:
        try:
            name = input("Client name: ")
            agency = input("Agency: ")
            number = input("Number: ")
            breakpoint()
            client = Client(name, None, None)
            account = CheckingAccount(client, agency, number)

            accounts.append(account)
        except KeyboardInterrupt:
            print(f"\n\n{len(accounts)}(s) created")
            sys.exit()


if __name__ == "__main__":
    __main__()
