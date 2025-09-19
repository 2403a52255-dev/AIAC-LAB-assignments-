import unittest
from task2 import grade

class TestGradeFunction(unittest.TestCase):
    def test_grade_A(self):
        self.assertEqual(grade(95), 'A')
        self.assertEqual(grade(90), 'A')

    def test_grade_B(self):
        self.assertEqual(grade(85), 'B')
        self.assertEqual(grade(80), 'B')

    def test_grade_C(self):
        self.assertEqual(grade(75), 'C')
        self.assertEqual(grade(70), 'C')

    def test_grade_D(self):
        self.assertEqual(grade(65), 'D')
        self.assertEqual(grade(60), 'D')

    def test_grade_F(self):
        self.assertEqual(grade(59), 'F')
        self.assertEqual(grade(0), 'F')

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            grade(-1)
        with self.assertRaises(ValueError):
            grade(101)

if __name__ == '__main__':
    unittest.main()