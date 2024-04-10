#Exercise 1
print(("Hello world\n" )*4)
#Exercise 2
print((99**3)*8)
#Exercise 3
a = bool(5 < 3)
print(f"5 < 3 is {a}")
b = bool(3 == 3)
print(f"3 == 3 is {b}")
c = bool(3 == "3")
print(f"3 == '3'is {c}")
print("'3' > 3 is a TypeError")
d = bool("Hello" == "hello")
print(f"'Hello' == 'hello' is {d}")
#Exercise 4
computer_brand = "dell"
print(f"I have a {computer_brand} computer")
#Exercise 5
name = "Geffen"
age = 26
shoe_size = 10
info = f"Hello, this is {name}, he is {age} years old and would like you to buy him a new set of blundstone boots in size {shoe_size}"
print(info)
#Exercise 6
a_1 = 9
b_1 = 3
if a_1 > b_1:
    print("Hello world")
#exercise 7
num = input("Please enter a number:")
if int(num) % 2 == 0:
    print(f"You entered {num}, which is even")
else:
    print(f"You entered {num}, which is odd")
#exercise 8
height = input("Please enter your height in centimeters:")
if int(height) > 145:
    print("You are tall enough to ride the rollercoaster; enjoy!")
else:
    print("I'm sorry you are not tall enough to ride the rollercoaster")