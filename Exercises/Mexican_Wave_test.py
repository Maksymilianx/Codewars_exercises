import unittest

from Exercises.Mexican_Wave import wave


class TestMexicanWave(unittest.TestCase):
    def test_volume_case1(self):
        result = ['Klops', 'kLops', 'klOps', 'kloPs', 'klopS']
        self.assertListEqual(wave('klops'),result)

    def test_volume_case2(self):
        result = ['Adbadfbafbf', 'aDbadfbafbf', 'adBadfbafbf', 'adbAdfbafbf', 'adbaDfbafbf', 'adbadFbafbf',
                  'adbadfBafbf', 'adbadfbAfbf', 'adbadfbaFbf', 'adbadfbafBf', 'adbadfbafbF']
        self.assertListEqual(wave('adbadfbafbf'),result)

    def test_volume_case3(self):
        result = ['Kupa', 'kUpa', 'kuPa', 'kupA']
        self.assertListEqual(wave('kupa'), result)

    def test_volume_case4(self):
        result = ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]
        self.assertListEqual(wave('two words'), result)

    def test_volume_case5(self):
        result = []
        self.assertListEqual(wave(""),result)

    def test_volume_case6(self):
        result = [" Gap ", " gAp ", " gaP "]
        self.assertListEqual(wave(' gap '), result)
