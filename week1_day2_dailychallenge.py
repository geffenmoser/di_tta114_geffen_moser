stringy = input("Please enter a word:")
if len(stringy) < 10:
    print("Your word is not long enough")
elif len(stringy) > 10:
    print("Your string is too long")
else:
    print("Perfect string")
stringy_first = stringy[0]
stringy_last = stringy [len(stringy)-1]
print(stringy_first + stringy_last)
n = ""
for c in stringy:
    n += c
    print(f"{n}\n")