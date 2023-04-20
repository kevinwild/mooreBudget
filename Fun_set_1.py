

def add_income(cash):
    while True:
        try:
            x = float(input('Enter just the number amount, or enter 0 to quit'))
            if isinstance(x, (int, float)) and x != 0.0:
                cash['Income'].append(float(x))
                print(cash)
            elif x == 0.0:
                return
        except Exception as e:
            print(e)


def add_expense(cash):
    while True:
        try:
            x = float(input('Enter just the number amount, or enter 0 to quit'))
            if isinstance(x, (int, float)) and x != 0.0:
                cash['Expense'].append(float(x))
                print(cash)
            elif x == 0.0:
                return
        except Exception as e:
            print(e)
