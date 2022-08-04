#!/usr/bin/env python

import sqlite3

print("Hello, from Messagediscovery.")
conn = sqlite3.connect("chat.db")
cursor = conn.cursor()
cursor.execute("select count(*) from message")
rows = cursor.fetchall()
cursor.close()
count = rows[0][0]

print(f"I found {count} total messages.")
print(5) 



