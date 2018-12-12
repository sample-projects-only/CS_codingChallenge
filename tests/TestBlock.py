import unittest
from Canvas import Canvas
from entities.Line import Line
from entities.Block import Block


class TestBlock(unittest.TestCase):

    def setUp(self):
        self.w = 5
        self.h = 4
        self.canvas = Canvas(self.w, self.h)

    def test__drawToCanvas(self):
        line = Line(3, 1, 3, 4)
        line.drawToCanvas()
        block = Block(1, 2, 'o')
        block.drawToCanvas()
        exp = [['o', 'o', 'x', ' ', ' '], ['o', 'o', 'x', ' ', ' '], ['o', 'o', 'x', ' ', ' '], ['o', 'o', 'x', ' ', ' ']]
        self.assertEqual(exp, self.canvas.canvasArray)

    def test_checkGeometryObjectConstraints(self):
        block1 = Block(1, 2)
        block2 = Block(6, 2)
        block3 = Block(1, 6)
        block4 = Block(-1, 2)
        block5 = Block(1, -1)

        self.assertEqual(True, block1.checkGeometryObjectConstraints())
        self.assertEqual(False, block2.checkGeometryObjectConstraints())
        self.assertEqual(False, block3.checkGeometryObjectConstraints())
        self.assertEqual(False, block4.checkGeometryObjectConstraints())
        self.assertEqual(False, block5.checkGeometryObjectConstraints())


if __name__ == '__main__':
    unittest.main()
