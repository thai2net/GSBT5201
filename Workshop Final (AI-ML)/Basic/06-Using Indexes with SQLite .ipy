# Optimizing Queries: Using Indexes with SQLite 

import sqlite3

# Connect to database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create table and index
cursor.execute('CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, value INTEGER)')
cursor.execute('CREATE INDEX IF NOT EXISTS idx_value ON data (value)')

# Insert data
cursor.executemany('INSERT INTO data (value) VALUES (?)', [(i,) for i in range(1000)])

# Query data
cursor.execute('SELECT * FROM data WHERE value = ?', (500,))
rows = cursor.fetchall()
print(rows)

conn.close()
