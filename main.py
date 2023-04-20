import csv
from Fun_set_1 import add_income
from Fun_set_1 import add_expense
cash = {
    "Income": [], 'Expense': [], 'type': []
}


def load_cflow_csv(csv_file_name):
    # Define the name of the CSV file
    global cash

    # Open the CSV file and read its contents
    with open(csv_file_name, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        # Iterate over each row in the CSV file
        for row in csv_reader:
            cash['Income'].append(row['Income'])
            cash['Expense'].append(row['Expense'])
            cash['type'].append(row['type'])


load_cflow_csv("cflow.csv")

wait = input('press enter to continue')


def transaction():
    cash['Income'] = [float(num) for num in cash['Income']]
    cash['Expense'] = [float(num) for num in cash['Expense']]
    print(cash)
    total = sum(cash['Income']) - sum(cash['Expense'])
    action = input(f'Hello, you have {total} in your account! What would you like to do ?'
                   f'\n [A] Input Income or Expense '
                   f'\n [B] Check balance or categorized expenses').lower()
    if action == 'a':
        tran_type = input('Expense or Income').lower()
        if tran_type == 'income':
            add_income(cash)
        elif tran_type == 'expense':
            add_expense(cash)
        else:
            print('you made an error try again')


while True:
    transaction()
