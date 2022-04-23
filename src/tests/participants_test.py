import unittest
from participants_repo import ParticipantsRepo
import os


class TestParticipants(unittest.TestCase):
    def setUp(self):
        filepath = os.path.join(os.path.dirname(
            __file__), "..", "data", "unittesting.csv")
        self.f = ParticipantsRepo(filepath)

    def test_empty_setup_ok(self):
        self.f = ParticipantsRepo()
        self.assertEqual(len(self.f.participants), 0)
        # should raise an exceptoin?

    def test_setup_from_file(self):
        self.assertEqual(len(self.f.participants), 8)
        self.assertEqual(len(self.f.return_has_wishes()), 6)
