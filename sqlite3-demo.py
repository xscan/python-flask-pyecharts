#coding=utf-8
import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()
print "Opened database successfully";

def init_db():
   c.execute('''CREATE TABLE COMPANY
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')
   print "Table created successfully";
   conn.commit()

def insert_data_db():
   c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
         VALUES (1, 'Paul', 32, 'California', 20000.00 )");
   c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
         VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");
   c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
         VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");
   c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
         VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");
   conn.commit()
   print "Records created successfully";

def select_db():
   cursor = c.execute("SELECT id, name, address, salary  from COMPANY")
   for row in cursor:
      print "ID = ", row[0]
      print "NAME = ", row[1]
      print "ADDRESS = ", row[2]
      print "SALARY = ", row[3], "\n"
      
   print "Operation done successfully";


init_db()
insert_data_db()
select_db()
conn.close()