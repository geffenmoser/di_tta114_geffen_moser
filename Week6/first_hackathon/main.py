import psycopg2
from tabulate import tabulate
from talmid import ChevrutaMaker

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'Gg1041gG'
DATABASE = 'talmidim_TTA'

# making the connection to the database
connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)


def register_talmid():
    yeshiva_list = []
    user_choice = input("Please enter 'n' to add a new Talmid or 'f' to complete the registration and return paired chevrutas:")
    n_talmid = []
    n_first = ''
    n_last = ''
    n_bochur = True
    is_bochur = ''
    is_slot1 = ''
    is_slot2 = ''
    is_slot3 = ''
    n_skill = 0
    n_interest = 0
    n_slot1 = True
    n_slot2 = True
    n_slot3 = True
    n_attendance = 0
    while user_choice != 'n' or 'f':
        user_choice = input(
            "Please enter 'n' to add a talmid or 'f' to complete pairing:")
        while user_choice != 'f':
            n_first = input("Please enter the Talmid's first name:")
            n_last = input(f"Please enter the {n_first}'s last name:")
            is_bochur = input(
                f"Please enter 'a' if {n_first} is married or 'b' if they are unmarried:")
            if is_bochur == 'a':
                n_bochur = False
            n_skill = input(
                f"Please rank {n_first}'s skill level with a number from 1 (beginner) to 10 (highly advanced):")
            n_interest = input(
                f"1=Gemara, 2=Halacha, 3=TaNaCh, 4=Chassidus, 5=Mussar\n Please enter {n_first}'s highest ranked interest from the list:")
            is_slot1 = input(
                f"Please enter 'u' if {n_first} is Not Available for learning "
                f"slot 1 or just press 'enter':")
            if is_slot1 == 'u':
                n_slot1 = False
            is_slot2 = input(
                f"Please enter 'u' if {n_first} is Not Available for learning slot 2 or just press 'enter':")
            if is_slot2 == 'u':
                n_slot2 = False
            is_slot3 = input(
                f"Please enter 'u' if {n_first} is Not Available for learning slot 3 or just press 'enter':")
            if is_slot3 == 'u':
                n_slot3 = False
            n_attendance = input(
                f"In numbers, how many zmanim has {n_first} been a Talmid here?:")
            n_talmid = [n_first, n_last, n_bochur, n_skill, n_interest, n_slot1,
                        n_slot2, n_slot3, n_attendance]
            yeshiva_list.append(n_talmid)
            break
        else:
            table_name = input("What is the Yeshiva's name?:")
            ChevrutaMaker.create_table(table_name)
            ChevrutaMaker.fill_table(table_name, yeshiva_list)
            ChevrutaMaker.pair_chevrutas(table_name)
    if user_choice != 'n' or 'f':
        print("Invalid choice, please restart")
register_talmid()




