expenses = [ ]

while True:
        amount = float(input("Enter amount: "))
        category = input("Enter category (food, gas, etc): ")

        expenses.append((amount, category))

        more = input("Add another? (y/n): ")
        if more.lower() == "n":
                break
        
# totals
total = 0
category_totals = {}

for amount, category in expenses:
            total+= amount

            if category in category_totals:
                    category_totals[category] += amount
            else:
                    category_totals[category] = amount

print("\n--- Spending summary ---")

for category, amount in category_totals.items():
        print(f"{category}: ${amount}")

print(f"\nTotal spent: ${total}")