#Reflection questions
#1. I did not expect that the first value in a list is zero instead of one. It was kind of confusing and also to go from back to front it is negitive -1 not 0.
#2. I have used excel for profit and loss before and it can be very teditous trying to find stuff within it. However, I have never came to a situation where I had to use python to in another class or internship and I am not too confident with it to say it is easier than excel.

# Excercise 1
print("---Excercise 1: Build the list ---")
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# Excercise 2
print("---Excercise 2: Index practice---")
print(inventory[0])
print(inventory[-1])

middle = len(inventory) // 2
print(inventory[middle])


#---excercise 3------
print("--- Excercise 3: List slicing ---")
print(inventory[:3]) 
print(inventory[-2:])
print(inventory[::2])

#---excercise 4------
print("--- Excercise 4: List methods ---")
inventory.append("envelope")
inventory.append("tape")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)

#---excercise 5------
print("--- Excercise 5: Tuple Campaision ---")
coords = (40.7128, -74.0060)

coords[0]
try:
    coords [0]
except TypeError as error:
    print(f"TypeError caught: {error}")
    print(f"Tuples protects cordinates from being changed by accident")


#---excercise 6------
print("--- Excercise 6: List average sales ---")
sales = [100,250,75,480,200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total sales: {total}")
print(f"Number of sales: {count}")
print(f"Average sales: {average}")
print(f"Best sale: {max(sales)}")
print(f"Worst sale: {min(sales)}")

best = sales[0]
worst = sales[0]

for amount in sales:
    if amount > best:
        best = amount
    if amount < worst:
        worst = amount
print(f"Best sale (loop): {best}")
print(f"Worst sale (loop): {worst}")

#-----excercise 7------
print("--- Excercise 7: Accumulator pattern ---")

prices = [9.99,14.99,4.99,24.99,1.99]

discounted = []
for price in prices:
    discounted.append(round(price* 0.9, 2))

print(prices)
print(discounted)

#----- excercise 8 ----
print("--- Excercise 8: Filter above threshold ---")
sales = [340,127,589,204,467,88,731,315,62,490]

high_sales = []

for amount in sales:
    if amount >300:
        high_sales.append (amount)
print(high_sales)
