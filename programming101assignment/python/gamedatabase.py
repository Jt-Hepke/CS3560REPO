import sqlite3

# create database and table
def create_database():
    conn = sqlite3.connect("rpg.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS player (
        id INTEGER PRIMARY KEY,
        health INTEGER,
        x INTEGER,
        y INTEGER
    )
    """)

    conn.commit()
    conn.close()

# save player data
def save_player(player):
    conn = sqlite3.connect("rpg.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM player")

    cursor.execute("""
    INSERT INTO player (health, x, y)
    VALUES (?, ?, ?)
    """, (player.health, player.x, player.y))

    conn.commit()
    conn.close()

# load player data
def load_player(player):
    conn = sqlite3.connect("rpg.db")
    cursor = conn.cursor()

    cursor.execute("SELECT health, x, y FROM player LIMIT 1")
    data = cursor.fetchone()

    if data:
        player.health = data[0]
        player.x = data[1]
        player.y = data[2]

    conn.close()