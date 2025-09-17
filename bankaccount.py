# TODO create class BankAccount

if __name__ == "__main__":
    # create BankAccount below this
    pass

class BankAccount:
    a = 0
    def __init__(self, _a = 0):
        global a
        a = _a

    def deposit(self, b):
        global a
        a += max(0,b)
        return a

    def withdraw(self, b):
        global a
        if a - b < 0:
            return "Insufficient Funds"
        a -= max(0,b)
        return a
    def get_balance(self):
        return a

