total = 0
expenses = []
num_expenses = int(input("Enter # of expenses:"))
for i in range(num_expenses):
    expenses.append(float(input("Enter an expenmse:")))

total =sum(expenses)

print("YOU FUCKING SPENT $", total, sep='')
