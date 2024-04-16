import unittest
import ImagePainter

class TestImagePainter(unittest.TestCase):
    def test_pixelStatus(self):
        self.assertEqual(ImagePainter.pixelStatus(1), '[100% =================================]')
        self.assertEqual(ImagePainter.pixelStatus(7), '[ 99% =================================]')
        self.assertEqual(ImagePainter.pixelStatus(257), '[ 50% ================                 ]')
        self.assertEqual(ImagePainter.pixelStatus(256), '[ 50% =================                ]')
        self.assertEqual(ImagePainter.pixelStatus(100), '[ 80% ===========================      ]')
        self.assertEqual(ImagePainter.pixelStatus(640), '[-25%                                  ]')
        self.assertEqual(ImagePainter.pixelStatus(137), '[ 73% ========================         ]')
        self.assertEqual(ImagePainter.pixelStatus(512), '[  0%                                  ]')
