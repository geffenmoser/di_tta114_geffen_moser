
python setup.py build
sudo python setup.py install
import psycopg2
# defining our connection criteria
HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'Gg1041gG'
DATABASE = 'talmidim_TTA'

# making the connection to the database
connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
cursor = connection.cursor()

def create_table(table_name):
    table_sql_command = f"CREATE TABLE {table_name}(talmid_id SERIAL PRIMARY KEY,                       first_name VARCHAR (50) NOT NULL,
                         last_name VARCHAR (100) NOT NULL,
                         bochur BOOLEAN NOT NULL,
                         skill_level SMALLINT NOT NULL,
                         interest_option SMALLINT NOT NULL,
                         timeslot_1 BOOLEAN NOT NULL,
                         timeslot_2 BOOLEAN NOT NULL,
                         timeslot_3 BOOLEAN NOT NULL)"
    