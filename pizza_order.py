print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, L \t")
add_pepperoni = input("Would you like to add Pepperoni? Y/N \t")
extra_cheese = input("Would you like extra cheese? Y/N \t")
s, m, l, = 15, 20, 25
total = 0

if size.upper() == "S":
    total = s
elif size.upper() == "M":
    total = m
elif size.upper() == "L":
    total = l
else:
    print("invalid input")

if add_pepperoni.upper() == "Y":
    if size.upper() == "S":
        total += 2
    else:
        total += 3

if extra_cheese.upper() == "Y":
    total += 1

print(f"Your final bill is £{total}")
