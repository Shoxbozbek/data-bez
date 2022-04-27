import sqlite3

num = sqlite3.connect('baza.db')

cursor = num.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS shop(
    name TEXT,
    last_name TEXT,
    age INTEGER
)


""")

cursor.execute("""
INSERT INTO shop VALUES
('SHOXBOZBEK','nematov',17 ),
('ghj','hgjhgj',17 ),
('SHOXBOZBEK','nematov',17 ),
('hj','nematov',17 ),
('SHOXBOZBEK','nematov',17 )

""")

cursor.execute("SELECT * FROM shop")
natija = cursor.fetchall()
print(natija)