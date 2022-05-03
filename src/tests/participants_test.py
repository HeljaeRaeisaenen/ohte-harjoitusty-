import unittest
from application_logic.participants_repo import ParticipantsRepo
import os


class TestParticipants(unittest.TestCase):
    def setUp(self):
        filepath = os.path.join(os.path.dirname(
            __file__), "..", "data", "unittesting.csv")
        self.f = ParticipantsRepo(filepath)

    def test_setup_from_file(self):
        self.assertEqual(len(self.f.get_participants()), 8)
        self.assertEqual(len(self.f.return_has_wishes()), 6)

    def test_return_full_name(self):
        name = "bananas"
        self.assertTrue(self.f.is_in_participants(name))
