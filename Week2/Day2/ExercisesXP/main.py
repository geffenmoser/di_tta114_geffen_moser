#Exercise 1
def display_message(*topics):
    print(f" I learned about the following topics today: {topics}")

display_message("functions", "lambdas")

#Exercise 2
def favorite_book(title):
    print(f"One of my favorite books is {title}")

favorite_book("Sherlock Holmes")

#Exercise 3
def describe_city(*city, country = "Israel"):
    if country == "Israel":
        print("Shalom")
    print(f"{city} is in {country}")

describe_city("Jerusalem")

#Exercise 4
import random
def rando_match(int):
    x  = random.randint(0, 100)
    if x == int:
        print(f"Success I randomly generated the same number as you ({int})")
    else:
        print(f"Fail, we picked different random numbers, I picked {x} and you picked {int}")

rando_match(32)

#Exercise 5
def make_shirt(size = "L", text = "I love Python"):
    print(f"The size of the shirt is '{size}' and it will say '{text}' on the front")

make_shirt("L", "This is a shirt")
make_shirt()
make_shirt("M", )
make_shirt("XXL", "I love cobras")

#Exercise 6
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians():
    for name in magician_names:
        print(f"{name}")
def make_magicians_great():
    i = 0
    for name in magician_names:
        print(f"{name} the Great")
        magician_names[i] += " the Great"
        i += 1
show_magicians()
make_magicians_great()
show_magicians()