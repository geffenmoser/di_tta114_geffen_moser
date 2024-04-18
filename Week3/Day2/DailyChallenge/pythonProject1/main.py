class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}
    def add_animal(self, added_animal, quant=1):
        if added_animal not in self.animals:
            self.animals[added_animal] = quant
        else:
            self.animals[added_animal] += quant
    def get_info(self):
        print(self.animals)
        print("E-I-E-I-0")

    def get_animal_types(self):
        return self.animals.keys()
    def get_short_info(self):
        start = self.get_animal_types()
        for x in start:
            if self.animals[x] >= 2:
                x = x + "s"
        print(f"{self.name}'s Farm has {start}")


macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_animal_types())
macdonald.get_short_info()