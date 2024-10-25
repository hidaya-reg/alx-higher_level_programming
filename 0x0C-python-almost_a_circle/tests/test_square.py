from modeltest.square import Square
import unittest
from unittest.mock import patch
from io import StringIO

class TestSquare(unittest.TestCase):

    def test_valid_atttr(self):
        s = Square(3, 1, 3, 10)

        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 3)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 3)
    
    def test_invalid_attrs(self):
        # non_integer size
        with self.assertRaises(TypeError):
            s = Square("9")
        
        # negative size
        with self.assertRaises(ValueError):
            s = Square(-5)

        # zero size
        with self.assertRaises(ValueError):
            s = Square(0)

        # non integer x
        with self.assertRaises(TypeError):
            s = Square(2, "1", 5)

        # negative x
        with self.assertRaises(ValueError):
            s = Square(2, -1, 6)

        # non integer y
        with self.assertRaises(TypeError):
            s = Square(2, 1, "f")

        # negative y
        with self.assertRaises(ValueError):
            s = Square(2, 1, -6)

    def test_auto_incr_id(self):
        s1 = Square(5)
        s2 = Square(45)

        self.assertEqual(s1.id + 1, s2.id)

    def test_area(self):
        s1 = Square(5)
        s2 = Square(2)

        self.assertEqual(s1.area(), 25)
        self.assertEqual(s2.area(), 4)
    
    def test_str(self):
        s1 = Square(5)
        self.assertEqual(str(s1), f"[Square] ({Square._Base__nb_objects}) 0/0 - 5")

        s2 = Square(3, 1, 3, 41)
        self.assertEqual(str(s2), "[Square] (41) 1/3 - 3")

    @patch('sys.stdout', new_callable=StringIO)
    def test_display(self, mock_stdout):
        s1 = Square(3)
        expected_output = "###\n###\n###\n"
        s1.display()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

        mock_stdout.truncate(0)
        mock_stdout.seek(0)

        s2 = Square(2, 2)
        expected_output = "  ##\n  ##\n"
        s2.display()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

        mock_stdout.truncate(0)
        mock_stdout.seek(0)

        s3 = Square(2, 3, 1)
        expected_output = "\n   ##\n   ##\n"
        s3.display()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_update(self):
        s1 = Square(5)
        self.assertEqual(str(s1), f"[Square] ({Square._Base__nb_objects}) 0/0 - 5")

        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")

        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")

        s1.update(1, 2, 3)
        self.assertEqual(str(s1), "[Square] (1) 3/0 - 2")

        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")

        s1.update(x=12)
        self.assertEqual(str(s1), "[Square] (1) 12/4 - 2")

        s1.update(size=7, y=1)
        self.assertEqual(str(s1), "[Square] (1) 12/1 - 7")

        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1), "[Square] (89) 12/1 - 7")

    def test_to_dictionary(self):
        s1 = Square(10, 2, 1, 1)
        s1_dict = s1.to_dictionary()
        self.assertIsInstance(s1_dict, dict)
        self.assertDictEqual(s1_dict, {'id': 1, 'x': 2, 'size': 10, 'y': 1})
        s2 = Square(1, 1)
        s2.update(**s1_dict)
        self.assertEqual(str(s1), str(s2))



if __name__ == "__main__":
    unittest.main()
