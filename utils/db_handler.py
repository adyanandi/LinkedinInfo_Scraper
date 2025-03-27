import sqlite3
import os
import json

def create_connection(db_file="output/linkedin_profiles.db"):
    os.makedirs("output", exist_ok=True)
    conn = sqlite3.connect(db_file)
    return conn

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS linkedin_profiles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            headline TEXT,
            location TEXT,
            about TEXT,
            experience TEXT,
            education TEXT,
            skills TEXT
        )
    ''')
    conn.commit()

def insert_profile_data(conn, data):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO linkedin_profiles (name, headline, location, about, experience, education, skills)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        data.get('Name'),
        data.get('Headline'),
        data.get('Location'),
        data.get('About'),
        '\n\n'.join(data.get('Experience') or []),
        "\n\n".join([str(i) for i in data.get("Education") or []]),
        ", ".join(data.get("Skills") or [])
    ))
    conn.commit()
