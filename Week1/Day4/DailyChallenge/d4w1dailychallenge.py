# ##challenge 1
# num = input("Please enter a number:")
# length = input("Please enter a length:")
# num = int(num)
# length = int(length)
# list1 = []
# new_num = num
# counter = length
# while counter >= 1:
#     list1.append(new_num)
#     new_num += num
#     counter -= 1
# print(list1)
#
# #challenge2
# stringle = input("type a word sllloooowwwlllyyy:")
# that_stringle = ''
# for i, char in enumerate(stringle):
#         if i == 0 or char != stringle[i-1]:
#             that_stringle += char
# print(that_stringle)
#
# ##exercise1
# my_fav_numbers = {15, 65, 26, 31}
# my_fav_numbers.add(17)
# my_fav_numbers.add(10)
# my_fav_numbers = set(list(my_fav_numbers)[:-1])
# friend_fav_numbers = {15,20,25}
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(my_fav_numbers)
# print(our_fav_numbers)
#
# #exercise2: No, more integers cannot be added to a tuple made of integers because a tuples are immutable
#
# #exercise3
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove("Banana")
# basket.remove("Blueberries")
# basket.append("Kiwi")
# print(basket)
# basket.insert(0, "Apples")
# print(basket)
# num_Apples = 0
# for n in basket:
#     if n == "Apples":
#         num_Apples += 1
# print(f"The number of Apples in the basket is {num_Apples}")
#
# ##Exercise 4
# ##1. A float is a string of numbers including decimals, since decimals cannot be represented as integers
# f_list = []
# for j in range (1,5):
#     f_list.append(float(j)+float(.5))
#     j += 1
#     f_list.append(j)
# print(f_list)
# ##3. The only other ways I have found to do it require mapping which I'm not familiar with yet or adding packages like 'math'
#
# ##Exercise 5
# for num in range(1,21):
#     print(num)
# for n in range(1,21):
#     if n % 2 == 0:
#         print(n)
# ##Exercise 6
# user_name = input("What is your name?")
# while user_name != "Geffen":
#     user_name = input("Really what's your name?")
#
# ##Exercise 7
# fruity = input("Tell me some of your favorite fruits and don't forget to separate entries with a single space:")
# fruit_list = fruity.split()
# print(fruit_list)
# new_fruit = input("Tell us a fruit:")
# a = True
# for fruit in fruit_list:
#     if fruit == new_fruit:
#         a = True
#         print("You chose one of your favorite fruits! Enjoy!")
#         break
#     else:
#         a = False
# if a is False:
#     print("You chose a new fruit. Enjoy!")
#
# #Exercise 8
# pizza_topping = input("tell us a pizza topping:")
# pizza_topping_list = []
# while pizza_topping != "quit":
#     pizza_topping_list.append(pizza_topping)
#     print(f"We will add {pizza_topping} to your pizza")
#     pizza_topping = input("tell us another pizza topping or enter 'quit':")
# pizza_price = 10.0 + (len(pizza_topping_list)*2.5)
# print(f"That will cost {pizza_price} dollars")
#
# #Exercise 9
# baby_tix = 0
# child_tix = 10
# adult_tix = 15
#
# order_a = int(input("How many people over 12 years old would like a movie ticket?"))
# order_c = int(input("How many children between 3 and 12 years old would like a movie ticket?"))
# order_b = int(input("How many babies under 3 years old would like a movie ticket?"))
#
# total_tix = (order_a*adult_tix)+(order_c*child_tix)
# print(f"that will cost {total_tix} dollars")
#
# teen_list = ["teen1", "teen2", "teen3"]
# permitted_teens = []
# for teen in teen_list:
#     age = int(input(f"what is {teen}'s age"))
#     if age <= 21:
#         print(f"{teen} is too young to enter this movie")
#     else:
#         permitted_teens.append(teen)
# print(f"{permitted_teens} are allowed to enter")
#
# #Exercise 10
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
i = 0
finished_sandwiches = []
while i <= len(sandwich_orders):
    if sandwich_orders[i] == "Pastrami sandwich":
        sandwich_orders.pop(i)
        i -= 1
    finished_sandwiches.append(sandwich_orders[i])
    print(f"I made your {sandwich_orders[i]}")
    sandwich_orders.pop(i)
    i += 1