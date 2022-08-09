import pymysql
import names
from faker import Faker

fake = Faker()

db = pymysql.connect(host='localhost', user='root', passwd='Qwerty123', db='indexes')

cur = db.cursor()

def create_structure(db, cursor):
    cursor.execute("CREATE TABLE IF NOT EXISTS users( id int auto_increment primary key, fullname varchar(20) null, create_date DATE null) ENGINE=InnoDB;");
    cursor.execute("CREATE TABLE IF NOT EXISTS users_indexes ( id int auto_increment primary key, fullname varchar(20) null, create_date varchar(20) null, create_date_hash varchar(20) null, create_date_btree varchar(20) null) engine = MEMORY;");
    cursor.execute("CREATE INDEX i_create_date_hash ON users_indexes (create_date_hash) USING hash;");
    cursor.execute("CREATE INDEX i_create_date_btree ON users_indexes (create_date_btree) USING btree;");

    db.commit()
    
def fill_db(db, cursor):    
    x = 40000000
    while x > 0:
        x -= 1
        cursor.execute("INSERT INTO `users` (`fullname`, `create_date`) VALUES (%s. %s)", (f"{names.get_first_name()} {names.get_last_name()}" , fake.date_between(start_date='-10y', end_date='today')));
    
    db.commit()      

def insert(cursor):    
    cursor.execute("INSERT INTO `users` (`fullname`, `create_date`) VALUES (%s. %s)", (f"{names.get_first_name()} {names.get_last_name()}", fake.date_between(start_date='-10y', end_date='today')));    

create_structure(db, cur)
fill_db(db, cur)

db.close()