#Exercise 2
from func import funcy_add

funcy_add(9,1000)

#exercise 3
import random
import string

def generate_random_string(length=5):
    letters = string.ascii_letters  # This contains both uppercase and lowercase letters
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

random_string = generate_random_string()
print(random_string)

#exercise 4
from datetime import datetime

x = datetime.now()
print(x)
#exercise 5

next_year = datetime(2025,1,1)

print(next_year - x)

#exercise 6
def calculate_minutes_lived(birthdate):
    birthdate_datetime = datetime.strptime(birthdate, '%Y-%m-%d')
    current_datetime = datetime.now()
    difference = current_datetime - birthdate_datetime
    minutes_lived = difference.total_seconds() / 60
    print(f"You have lived approximately {int(minutes_lived):,} minutes in your life.")

calculate_minutes_lived("1997-10-25")

#exercise 7
pip install faker
from faker import Faker
fake = Faker()
users = []
def add_user(users_list):
    user = {
        'name': fake.name(),
        'address': fake.address(),
        'language_code': fake.language_code()
    }
    users_list.append(user)
for _ in range(5):
    add_user(users)
for user in users:
    print(user)
