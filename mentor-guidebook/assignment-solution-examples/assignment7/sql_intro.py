import sqlite3

def create_publisher(cursor, name):
    try:
        cursor.execute("INSERT INTO publishers (name) VALUES (?);", (name,))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

def create_magazine(cursor, name, publisher):
    cursor.execute("SELECT id FROM publishers WHERE name = (?);", (publisher,))
    results = cursor.fetchall()
    if len(results) == 0:
        print("That publisher was not found in the database.")
        return
    publisher_id = results[0][0]
    try:
        cursor.execute("INSERT INTO magazines (name, publisher_id) VALUES (?, ?);", (name,publisher_id))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

def create_subscriber(cursor, name, address):
    cursor.execute("SELECT id FROM subscribers WHERE name = ? AND address = ?;", (name,address))    
    results = cursor.fetchall()
    if len(results) > 0:
        print("That subscriber was already in the database.")
        return   
    cursor.execute("INSERT INTO subscribers (name, address) VALUES (?,?);", (name,address))  

def create_subscription(cursor, name, address, magazine, expiration):
    cursor.execute("SELECT id FROM subscribers WHERE name =? AND address = ?;", (name,address))    
    results = cursor.fetchall()
    if len(results) == 0:
        print("That subscriber was not found in the database.")
        return
    subscriber_id = results[0][0]
    cursor.execute("SELECT id FROM magazines WHERE name = ?;", (magazine,))    
    results = cursor.fetchall()
    if len(results) == 0:
        print("That magazine was not found in the database.")
        return
    magazine_id = results[0][0]
    cursor.execute("SELECT id FROM subscriptions WHERE subscriber_id = ? AND magazine_id = ?;", (subscriber_id,magazine_id))    
    results = cursor.fetchall()
    if len(results) > 0:
        print("That subscription was already in the database.")
        return
    cursor.execute("INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?);", (subscriber_id, magazine_id, expiration))

# Connect to the database
with sqlite3.connect("../db/magazines.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1") # This turns on the foreign key constraint
    cursor = conn.cursor()

    # Create tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS publishers (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS magazines (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        publisher_id INTEGER,
        FOREIGN KEY (publisher_id) REFERENCES publishers (id)    
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscribers (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        address TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscriptions (
        id INTEGER PRIMARY KEY,
        magazine_id INTEGER,
        subscriber_id INTEGER,
        expiration_date TEXT NOT NULL,
        FOREIGN KEY (magazine_id) REFERENCES magazines (id),
        FOREIGN KEY (subscriber_id) REFERENCES subscribers (id)
    )
    """)

    print("Tables created successfully.")
    create_publisher(cursor,"Acme")
    create_publisher(cursor,"Megabucks")
    create_publisher(cursor,"Mostly True")
    create_magazine(cursor,"Yellow Press", "Acme")
    create_magazine(cursor,"Sensation", "Mostly True")
    create_magazine(cursor,"Silly Stuff", "Acme")
    create_subscriber(cursor, 'John Public', '123 peachtree street')
    create_subscriber(cursor, "Ellen Whatever", '7 North Main')
    create_subscriber(cursor, 'Wes Western', 'P.O. Box 19')
    create_subscription(cursor,'John Public', '123 peachtree street', 'Sensation', 'June 7, 2026')
    create_subscription(cursor,'John Public', '123 peachtree street', 'Silly Stuff', 'June 7, 2026')
    create_subscription(cursor, "Ellen Whatever", '7 North Main', 'Yellow Press', 'June 7, 2026')
    conn.commit()
    cursor.execute("SELECT * FROM subscribers;")
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.execute("SELECT * FROM magazines ORDER BY name;")
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.execute("SELECT * FROM publishers p JOIN magazines m on p.id = m.publisher_id WHERE p.name = 'Acme';")
    results = cursor.fetchall()
    for row in results:
        print(row)

