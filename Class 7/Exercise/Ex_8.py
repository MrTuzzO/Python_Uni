class Calculator:
    def add(self, *args):
        return sum(args) if args else 0

calc = Calculator()
print(calc.add(1, 2, 4, 8, 9))
print(calc.add(6))

