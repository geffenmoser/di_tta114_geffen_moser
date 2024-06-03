import psycopg2
from tabulate import tabulate
from talmid import ChevrutaMaker

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'Gg1041gG'
DATABASE = 'talmidim_TTA'

# making the connection to the database
connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)

def get_user_menu_choice():
    menu_choice = input("Please enter 'n' to add a new Talmid or 'f' to complete the registration and return paired chevrutas:")
    if menu_choice == "n" or "f":
        return menu_choice
    else:
        print("You made an invalid choice")
        menu_choice = input("Please select only 'n' to add a new Talmid or 'f' to complete the registration and return paired chevrutas:")

def register_talmid():
    yeshiva_list = []
    user_menu_choice = get_user_menu_choice()
    n_talmid = []
    n_first = ''
    n_last = ''
    n_bochur = True
    is_bochur = ''
    is_slot1 = ''
    is_slot2 = ''
    is_slot3 = ''
    n_interest = ''
    n_skill = 0
    n_int = 0
    n_slot1 = True
    n_slot2 = True
    n_slot3 = True
    while user_menu_choice != 'f':
        n_first = input("Please enter the Talmid's first name:")
        n_last = input(f"Please enter the {n_first}'s last name:")
        is_bochur = input(
            f"Please enter 'a' if {n_first} is married or 'b' if they are unmarried:")
        if is_bochur == 'a':
            n_bochur = False
        elif is_bochur == 'b':
            n_bochur = True
        n_skill = input(
            f"Please rank {n_first}'s skill level with a number from 1 (beginner) to 10 (highly advanced):")
        n_int = input(
            f"1=Gemara, 2=Halacha, 3=TaNaCh, 4=Chassidus, 5=Mussar\n Please enter {n_first}'s highest ranked interest from the list:")
        is_slot1 = input(
            f"Please enter 'u' if {n_first} is Not Available for learning "
            f"slot 1 or just press 'enter':")
        if is_slot1 == 'u':
            n_slot1 = False
        elif is_slot1 == '':
            n_slot1 = True
        is_slot2 = input(
            f"Please enter 'u' if {n_first} is Not Available for learning slot 2 or just press 'enter':")
        if is_slot2 == 'u':
            n_slot2 = False
        elif is_slot2 == '':
            n_slot2 = True
        is_slot3 = input(
            f"Please enter 'u' if {n_first} is Not Available for learning slot 3 or just press 'enter':")
        if is_slot3 == 'u':
            n_slot3 = False
        elif is_slot3 == '':
            n_slot3 = True
        if n_int == '1':
            n_interest = 'Gemara'
        elif n_int == '2':
            n_interest = 'Halacha'
        elif n_int == '3':
            n_interest = 'TaNaCh'
        elif n_int == '4':
            n_interest = 'Chassidus'
        elif n_int == '5':
            n_interest = 'Mussar'
        n_talmid = [n_first, n_last, n_bochur, n_skill, n_interest, n_slot1,
                    n_slot2, n_slot3]
        yeshiva_list.append(n_talmid)
        user_menu_choice = get_user_menu_choice()
    else:
        table_name = input("What is the Yeshiva's name?:")
        ChevrutaMaker.create_table(table_name)
        ChevrutaMaker.fill_table(table_name, yeshiva_list)
        ChevrutaMaker.pair_chevrutas(table_name)

register_talmid()

