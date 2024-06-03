import psycopg2
from tabulate import tabulate

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'Gg1041gG'
DATABASE = 'talmidim_TTA'

# making the connection to the database
connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
class ChevrutaMaker:
    yeshiva_list = []

    def create_table(talmid_table):
        cursor = connection.cursor()
        create_table_command = f'''DROP TABLE IF EXISTS {talmid_table};
        CREATE TABLE {talmid_table} (talmid_id 
        SERIAL PRIMARY
        KEY,
                             first_name VARCHAR (50) NOT NULL,
                             last_name VARCHAR (100) NOT NULL,
                             bochur BOOLEAN NOT NULL,
                             skill_level SMALLINT NOT NULL,
                             interest_option VARCHAR(50) NOT NULL,
                             slot_1 BOOLEAN NOT NULL,
                             slot_2 BOOLEAN NOT NULL,
                             slot_3 BOOLEAN NOT NULL)'''
        cursor.execute(create_table_command)
        connection.commit()
    def return_table(talmid_table):
        cursor = connection.cursor()
        select_table_command = f'''SELECT * FROM {talmid_table}'''
        cursor.execute(select_table_command)
        output = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]
        output = tabulate(output, headers=column_names, tablefmt='psql')
        connection.commit()
        cursor.close()
        return output
    def fill_table(talmid_table, yeshiva_list):
        cursor = connection.cursor()
        for x in range(len(yeshiva_list)):
            insert_table_command = f''' INSERT INTO {talmid_table} (first_name, 
            last_name, bochur, skill_level, interest_option, slot_1, slot_2, 
            slot_3) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''
            cursor.execute(insert_table_command, yeshiva_list[x])
            connection.commit()
        output = ChevrutaMaker.return_table(talmid_table)
        print(f'Here is the filled table \n {output}')
        cursor.close()
    def sort_chevrutas(talmid_table):
        cursor = connection.cursor()

        sort_and_group_chevrutas = f'''
                SELECT * FROM {talmid_table}
                ORDER BY interest_option, skill_level, slot_1, slot_2, slot_3;
                '''

        cursor.execute(sort_and_group_chevrutas)
        connection.commit()
        cursor.close()
    def pair_chevrutas(talmid_table):
        column_pair_id = f'''ALTER TABLE {talmid_table} ADD COLUMN chevruta_id INT'''
        column_pair_set = f'''UPDATE {talmid_table} SET chevruta_id = FLOOR((
        talmid_id 
        - 1) / 2) + 1;'''
        cursor.execute(column_pair_id)
        cursor.execute(column_pair_set)
        connection.commit()
        output = ChevrutaMaker.return_table(talmid_table)
        print(f'Here is your chevruta matched table \n {output}')
        cursor.close()