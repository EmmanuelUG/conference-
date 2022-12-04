

from multiprocessing import connection
import sqlite3
import csv

connection = sqlite3.connect("conferences.db")
cursor = connection.cursor()

# creating the table in the database


cursor.execute("""CREATE TABLE IF NOT EXISTS halls (
                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    halls TEXT,
                    seats INTEGER,
                    price INTEGER,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
                )""")

cursor.execute("""
               CREATE TABLE IF NOT EXISTS customers (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   phone_number TEXT
               );
               """)

cursor.execute("""
               CREATE TABLE IF NOT EXISTS bookings (
                   id INTEGER PRIMARY KEY AUTOINCREMENT, 
                   customer_id INTEGER NOT NULL REFERENCES customers(id),
                   content TEXT,
                   total INTEGER
               );
               """)
print("database has been created")

def populate_db():
    with open("conference.csv")as file:
        data = csv.reader(file)
        next(data,None)
        cursor.executemany(
            "INSERT INTO halls('halls','seats','price') VALUES(?,?,?)",data)
        
def view_db():
    cursor.execute("SELECT * from halls")
    db_content = cursor.fetchall()
    return db_content
    

