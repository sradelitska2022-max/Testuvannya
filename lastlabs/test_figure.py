
# test_figure.py

import unittest
from random import choice, randint
from app import Figure

class TestFigure(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Runs once at the beginning"""
        pass

    def setUp(self) -> None:
        """Runs before each test"""
        self.figure_type = choice(Figure.FIGURES)
        self.length = randint(1, 10)
        self.obj = Figure(self.figure_type, self.length)
        return super().setUp()

    def tearDown(self) -> None:
        del self.obj
        return super().tearDown()

    def test_figure_type(self):
        print(f"Testing type: {self.figure_type} == {self.obj.get_figure_type}")
        self.assertEqual(self.figure_type, self.obj.get_figure_type,
                         "Property get_figure_type returns wrong figure!")

    def test_figure_length(self):
        self.assertEqual(self.length, self.obj.get_figure_length,
                         "Property get_figure_length returns wrong length!")

    def test_invalid_figure(self):
        with self.assertRaises(AssertionError):
            Figure("circle", 1)  

if __name__ == '__main__':
    unittest.main() 
