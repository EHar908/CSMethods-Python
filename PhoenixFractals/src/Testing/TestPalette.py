import unittest
from Palette import PaletteOne, PaletteTwo

class TestPalette(unittest.TestCase):
    def setUp(self):
        self.pal1Size120 = PaletteOne(120)
        self.pal2Size130 = PaletteTwo(130)
        self.pal1Size240 = PaletteOne(240)
        self.pal2Size260 = PaletteTwo(260)
        self.pal1Size360 = PaletteOne(360)
        self.pal2Size390 = PaletteTwo(390)
        self.pal1Size111 = PaletteOne(111)
        self.pal2Size111 = PaletteTwo(111)

    def test_paletteReturnString(self): #Because we're dividing up the given iterations in the function
        self.assertEqual(type(self.pal1Size120.getColor(1)), str)
        self.assertEqual(type(self.pal2Size130.getColor(3)), str)
        self.assertEqual(type(self.pal1Size111.getColor(55)), str)
        self.assertEqual(type(self.pal2Size111.getColor(110)), str)


    def test_paletteExpectedLength(self): #Verifying that the division is at least going correctly and that the combined lengths
        self.assertEqual(len(self.pal1Size120.dynamic), 120)
        self.assertEqual(len(self.pal2Size130.dynamic), 130)
        self.assertEqual(len(self.pal1Size240.dynamic), 240)
        self.assertEqual(len(self.pal2Size260.dynamic), 260)
        self.assertEqual(len(self.pal1Size360.dynamic), 360)
        self.assertEqual(len(self.pal2Size390.dynamic), 390)

if __name__ == '__main__':
    unittest.main()

