import os
import sqlite3

database_name = 'db_hw3.sqlite3'
DEFAULT_PATH = os.path.join(os.path.dirname(__file__), database_name)


def init_database():
    """
    Create database in current folder.
    Create table 'customers' with columns 'id', 'FirstName', 'LastName'.
    Create table 'tracks' with columns 'id', 'TracksName', 'genre', 'TrackLength'.
    """
    with sqlite3.connect(DEFAULT_PATH) as conn:
        with conn as cursor:
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS customers 
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                FirstName VARCHAR(255) NOT NULL,
                LastName VARCHAR(255) UNIQUE NOT NULL)"""
            )
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS tracks 
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                TracksName VARCHAR(255) UNIQUE NOT NULL,
                genre VARCHAR(255) NOT NULL,
                TrackLength FLOAT NOT NULL DEFAULT 0)"""
            )


def exec_query(query, *args):
    with sqlite3.connect(DEFAULT_PATH) as conn:
        with conn as cursor:
            qs = cursor.execute(query, args)
            results = qs.fetchall()
    return results


if __name__ == "__main__":
    init_database()
