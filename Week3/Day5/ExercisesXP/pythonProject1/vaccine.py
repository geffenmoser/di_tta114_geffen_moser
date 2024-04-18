#part1
class Human:
    def __init__(self, id_number, name, age=0, priority=False, blood_type):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type
class Queue(Human):
    qlist = []
    def add_person(self, person):
        global qlist
        if person.age >= 60:
            person.priority = True
            qlist.insert(0, person)
        else:
            qlist.append(person)
    def find_in_queue(self, person):
        in_line = qlist.index(person)
        return in_line
    def swap(self, person1, person2):
        qlist[person2], qlist[person1] = qlist[person1], qlist[person2]
    def get_next(self):
        return qlist[0]
    def get_next_blood_type(self, blood_type):
        for persons in qlist:
            if persons.blood_type == blood_type:
                return persons
            else:
                return None
    def sort_by_age(self):
        sorted(qlist, key=lambda person:person.priority = True)
        sorted(qlist, key=lambda person:person.age, reverse = True)

#part2


