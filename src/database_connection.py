'''Create database connection.'''
import os
import sqlite3
from pathlib import Path


def get_database_connection():
    '''Creates and returns a database connection.'''
    dirname = os.path.dirname(__file__)

    try:
        connection = sqlite3.connect(os.path.join(
            dirname, "data", "login_database.sqlite"))
        connection.row_factory = sqlite3.Row
    except FileNotFoundError:
        Path(os.path.join(
            dirname, "data", "login_database.sqlite")).touch()
        connection = sqlite3.connect(os.path.join(
            dirname, "data", "login_database.sqlite"))
        connection.row_factory = sqlite3.Row
    return connection


def close_database_connection(connect):
    '''Close a database.'''
    connect.close()
