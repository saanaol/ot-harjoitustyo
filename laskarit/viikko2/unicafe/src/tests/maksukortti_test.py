import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_salso_on_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(200)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 12.00 euroa")

    def test_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(200)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 8.00 euroa")

    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1100)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_metodi_palauttaa_oikean_totuusarvon_false(self):
        paluuarvo = self.maksukortti.ota_rahaa(1100)

        self.assertEqual(paluuarvo, False)
    
    def test_metodi_palauttaa_oikean_totuusarvon_true(self):
        paluuarvo = self.maksukortti.ota_rahaa(900)

        self.assertEqual(paluuarvo, True)
