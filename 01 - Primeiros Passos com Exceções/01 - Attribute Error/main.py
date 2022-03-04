class Client:
    def __init__(self, name, cpf, profession):
        self.name = name
        self.cpf = cpf
        self.profession = profession

    def __str__(self):
        return f"Name: {self.name}, CPF: {self.cpf}, Profession: {self.profession}"


def __main__():
    c1 = Client("Joe", "3457348534", "Programmer")

    print(c1)
    print(c1.age)


if __name__ == "__main__":
    __main__()
