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
        self.balance = 100
        self.client = client
        self.agency = agency
        self.number = number

        CheckingAccount.total_accounts_created += 1
        CheckingAccount.operation_tax = 30 / CheckingAccount.total_accounts_created

    def transfer(self, value, favored):
        favored.deposit(value)

    def withdraw(self, value):
        self.balance -= value

    def deposit(self, value):
        self.balance += value


def __main__():
    pass


if __name__ == "__main__":
    __main__()
