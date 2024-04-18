#exercise 1
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

def find_oldest_cat(list_of_cats):
    max = 0
    max_index = 0
    for cat in list_of_cats:
        i = 0
        if cat.age > max:
            max = cat.age
            max_index = i
        i += 1
    return list_of_cats[max_index]


george = Cat("George", 14)
kit = Cat("Kit", 3)
bob = Cat("Bob", 10)
cat_house = [george, kit, bob]
old_cat = find_oldest_cat(cat_house)
print(f"The oldest cat is {old_cat.name}, and is {old_cat.age} years old.")

#exercise 2
class Dog:
    def __init__(self, dog_name, dog_height):
        self.name = dog_name
        self.height = dog_height

    def bark(self):
        print(f"{self.name} goes woof!")
    def jump(self):
        print(f"{self.name} jumps {self.height*2} cm high")

davids_dog = Dog("Rex", 50)
print(davids_dog.name)
print(davids_dog.height)
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup", 20)
print(sarahs_dog.name)
print(sarahs_dog.height)
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is the bigger dog")
else:
    print(f"{sarahs_dog.name} is the bigger dog")

#exercise 3
class Song:
    def __init__(self, lyrics_list):
        self.lyrics = lyrics_list
    def sing_me_a_song(self):
        for x in self.lyrics:
            print(f"{x}\n")
stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()

#exercise 4
class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self, *new_animals):
        for animal in new_animals:
            if animal not in self.animals:
                self.animals.append(animal)
    def get_animals(self):
        print(self.animals)
    def sell_animal(self, *animal_sold):
        for x in animal_sold:
            if x in self.animals:
                self.animals.remove(x)
    def sort_animals(self):
        sorted_animal = []
        x = []
        for i in self.animals:
            if i[0] not in x:
                x.append(i[0])
        for i in x:
            group = []
            for j in self.animals:
                if j[0]==i:
                    group.append(j)
            sorted_animal.append(group)
        return sorted_animal
    def get_groups(self):
        print(self.sort_animals())


ramat_gan_safari = Zoo("Ramat Gan Zoo")
ramat_gan_safari.add_animal("giraffe", "ape", "elephant", "baboon", "gopher", "bear")
ramat_gan_safari.sell_animal("ape")
ramat_gan_safari.get_animals()
ramat_gan_safari.get_groups()