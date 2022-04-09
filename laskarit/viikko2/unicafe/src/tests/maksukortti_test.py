import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_rahaa_oikea_maara(self):
        self.assertEqual(self.maksukortti.saldo, 10)

    def test_lataa_rahaa_oikiein(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(self.maksukortti.saldo, 20)


    def test_rahan_poisto_oikein(self):
        self.assertEqual(self.maksukortti.ota_rahaa(5), True)
        self.assertEqual(self.maksukortti.saldo, 5)

    def test_saldo_ei_negatiiviseksi(self):
        self.assertEqual(self.maksukortti.ota_rahaa(11), False)
        self.assertEqual(self.maksukortti.saldo, 10)


    def test_str(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")