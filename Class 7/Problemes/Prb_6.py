class Calculator:
    def addition(self, *args):
        return sum(args) if args else 0


calculator = Calculator()
print(calculator.addition(1, 2, 3))
print(calculator.addition(5, 6))