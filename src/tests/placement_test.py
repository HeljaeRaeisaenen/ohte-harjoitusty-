import unittest
from placement import Placement


class TestPlacement(unittest.TestCase):
    def setUp(self):
        self.p = Placement(
            1, "/home/raisaneh/k/ohte/ohte_harjo/src/data/unittesting.csv")

    def test_initialize(self):
        self.assertEqual(self.p.tables, 1)
        self.assertEqual(len(self.p.file.names), 8)
        self.assertEqual(len(self.p.file.firstnames), len(self.p.file.names))
        self.assertEqual(self.p.friendgroups, [])
        self.assertLessEqual(len(self.p.file.wishes), len(self.p.file.names))

    def test_create_friendgroup(self):
        name = self.p.file.names[0]
        luck = self.p.create_friendgroup(0)
        '''at this point, whether create_friendgroup() will succeed or fail is unpredictable to me :D'''
        if luck == "Bad luck":
            # ooops
            return
        if luck == "ok":
            self.assertTrue(self.p.file.placed[0])
            self.assertEqual(len(self.p.friendgroups), 1)
            #self.assertNotIn(None, self.p.friendgroups[0])

    def test_create_friendgroup_bound_to_fail(self):
        self.p.file.names.insert(0, "Peas -")
        self.p.file.wishes.insert(0, ["Carrots -"])
        self.p.file.firstnames.insert(0, "Peas")
        self.p.file.placed.append(False)
        x = self.p.create_friendgroup(0)
        print(self.p.friendgroups)
        self.assertEqual(x, "Bad luck")

    def test_create_friendgroup_onewish(self):
        pass

    def test_create_friendgroup_everyone(self):
        pass

    def test_create_friendroup_fromfirstnames(self):
        pass
    # rememnber lowercase
