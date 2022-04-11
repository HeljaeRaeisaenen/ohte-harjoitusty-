import unittest
from participants import Participants


class TestParticipants(unittest.TestCase):
    def setUp(self):
        self.f = Participants(
            "/home/raisaneh/k/ohte/ohte_harjo/src/data/unittesting.csv")

    def test_empty_setup_ok(self):
        self.f = Participants()
        self.assertEqual(self.f.names, [])
        self.assertEqual(self.f.wishes, [])

    def test_setup_from_file(self):
        self.assertEqual(len(self.f.names), 8)
        self.assertEqual(len(self.f.wishes), 6)
