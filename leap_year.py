year = int(input("what year would you like to check? \t"))
is_div4 = year % 4
is_div100 = year % 100
is_div400 = year % 400
is_leap = ''

if is_div4 < 1:
    is_leap = True
    if is_div100 < 1:
        is_leap = False
        if is_div400 < 1:
            is_leap = True

else:
    is_leap = False

print(f"{year} is a leap year? {is_leap}")
