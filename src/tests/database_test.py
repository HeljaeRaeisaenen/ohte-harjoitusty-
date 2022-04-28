import sqlite3
import os
from pathlib import Path
import unittest
from database_functions import Logging


class TestParticipants(unittest.TestCase):
    def setUp(self):
        dirname = os.path.dirname(__file__)

        Path(os.path.join(
            dirname, "..", "data", "login_database.sqlite"))
        connection = sqlite3.connect(os.path.join(
            dirname, "..", "data", "test_database.sqlit"))
        connection.row_factory = sqlite3.Row
        self.l = Logging(connection)
    
    def test_name_not_saved(self):
        name = "Jaakko"
        x = self.l.find_username(name)
        self.assertFalse(x)
    
    def test_name_saved(self):
        name = "AAAAA"
        self.l.create_username(name, "123")
        x = self.l.find_username(name)
        self.assertTrue(x)
    
    def test_view_statistics(self):
        name = "AAAAA"
        self.l.create_username(name, "123")
        x = self.l.view_statistics(name)
        self.assertIsNone(x[0])
        self.assertIsNone(x[1])
    
    def test_username_password(self):
        name = "AAAAA"
        self.l.create_username(name, "123")
        x = self.l.verify_password(name, "123")
        self.assertTrue(x)