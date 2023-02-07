class Account:
    # constructor
    def __init__(self, name, pin):
        # instance variables
        self._pin = pin
        self._name = name
        self._balance = 0

    #     methods and parameters
    def check_balance(self, pin):
        if pin == self._pin:
            return self._balance

    def deposit(self, amount):
        self._balance += amount
        return self._balance
    #   self.account

    def withdraw(self, amount):
        self._balance -= amount