expenses = [ ]

while True:
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")

        expenses.append((amount, category))

        again = input("Add another? (y/n): ")

        if again == "n":
            break
            
total = 0

for expense in expenses:
    total += expense[0]

print ("Total spent:", total)