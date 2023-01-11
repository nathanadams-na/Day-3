your_name = input("Please enter your your_name \t")
their_name = input("Please enter their name \t")
your_name_list = list(your_name.lower())
their_name_list = list(their_name.lower())
true_love = "truelove"
percent1 = 0
percent2 = 0

for letters in true_love:
    # print(your_name)
    # print(f"{your_name.count(letters)} , {letters}")
    # print(their_name)
    # print(f"{their_name.count(letters)} , {letters}")
    percent1 += your_name.count(letters)
    percent2 += their_name.count(letters)

score = int(str(percent1) + str(percent2))
if score < 10 or score > 90:
    print(f"Your score is {score}%, you go together like coke and mentos.")
elif 40 <= score <= 50:
    print(f"Your score is {score}%, you are alright together")
else:
    print(f"your score is {score}%")

# for x in name_list:
# print(your_name.count(x))
# letterscount = {}
# for letters in name_list:
#    letterscount[letters] = letterscount.get(letters, 0) + 1
# print(letterscount)
