import unittest
from placement import Placement
import os


class TestPlacement(unittest.TestCase):
    def setUp(self):
        filepath = os.path.join(os.path.dirname(
            __file__), "..", "data", "unittesting.csv")
        self.p = Placement(1, filepath)

    def test_initialize(self):
        self.assertEqual(self.p.tables_n, 1)
        self.assertEqual(len(self.p.repo.participants), 8)
        self.assertEqual(len(self.p.fin_placement), 1)

    def test_create_friendgroup(self):
        name = "Apples -"
        self.p.create_friendgroup(name)
        x = [self.p.repo.participants[name].on_the_left,
             self.p.repo.participants[name].on_the_right,
             self.p.repo.participants[name].opposite]
        while None in x:
            x.remove(None)
        self.assertEqual(len(x), 3)

    def test_is_placed_called_always(self):
        name = "Apples -"
        self.p.create_friendgroup(name)
        x = self.p.repo.return_not_placed()
        self.assertNotIn("Bananas -", x)
        self.assertNotIn("Cherries -", x)
        self.assertNotIn("Horseradish -", x)

    def test_create_friendgroup_bound_to_fail(self):
        filepath = os.path.join(os.path.dirname(
            __file__), "..", "data", "unittesting_additional.csv")
        self.p.repo.initialize(filepath)
        self.assertIn("Peas -", self.p.repo.participants)
        self.p.create_friendgroup("Peas -")
        x = [self.p.repo.participants["Peas -"].on_the_left,
             self.p.repo.participants["Peas -"].on_the_right,
             self.p.repo.participants["Peas -"].opposite]
        while None in x:
            x.remove(None)
        self.assertEqual(len(x), 0)

    def test_create_friendgroup_onewish(self):
        # self.setUp()
        name = "Figs -"
        self.p.create_friendgroup(name)
        x = [self.p.repo.participants[name].on_the_left,
             self.p.repo.participants[name].on_the_right,
             self.p.repo.participants[name].opposite]
        while None in x:
            x.remove(None)
        self.assertEqual(len(x), 1)

    def test_create_fromfirstnames(self):
        name = "Bananas -"
        x = self.p.repo.participants[name].wishes
        self.assertGreaterEqual(len(x), 1)
        self.assertIn("Dragonfruits -", x)

    def test_create_tables(self):
        filepath = os.path.join(os.path.dirname(
            __file__), "..", "data", "testi.csv")
        self.p.repo.initialize(filepath)
        self.p = Placement(1, filepath)
        self.assertEqual(len(self.p.fin_placement), 1)
        self.assertGreaterEqual(len(self.p.fin_placement[0][0])*2, 42)

        filepath = os.path.join(os.path.dirname(
            __file__), "..", "data", "testi.csv")
        self.p.repo.initialize(filepath)
        self.p = Placement(2, filepath)
        self.assertEqual(len(self.p.fin_placement), 2)
        x = (len(self.p.fin_placement[0][1]) * 2) + \
            (len(self.p.fin_placement[1][1]) * 2)
        self.assertGreaterEqual(x, 42)
