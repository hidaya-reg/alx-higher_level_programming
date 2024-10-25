import unittest
from modeltest.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch
from models.base import Base

class TestRectangle(unittest.TestCase):
    
    def test_autoincrement_id(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)

        self.assertEqual(r1.id + 1, r2.id)

    def test_id_provided(self):
        r3 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(r3.id, 12)

    def test_valid_attributes(self):
        r = Rectangle(10, 20, 1, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
    
    def test_invalid_width(self):
        # Non integer width
        with self.assertRaises(TypeError):
            Rectangle("10", 20)
        
        # Negative integer width
        with self.assertRaises(ValueError):
            Rectangle(-10, 20)

        # Zero width
        with self.assertRaises(ValueError):
            Rectangle(0, 20)

    def test_invalid_height(self):
        # Non integer height
        with self.assertRaises(TypeError):
            Rectangle(10, "20")
        
        # Negative integer height
        with self.assertRaises(ValueError):
            Rectangle(10, -20)

        # Zero height
        with self.assertRaises(ValueError):
            Rectangle(10, 0)

    def test_invalid_x(self):
        # Non integer x
        with self.assertRaises(TypeError):
            Rectangle(10, 20, "1")
        
        # Negative integer x
        with self.assertRaises(ValueError):
            Rectangle(10, 20, -5)

    def test_invalid_y(self):
        # Non integer y
        with self.assertRaises(TypeError):
            Rectangle(10, 20, 1, "2")
        
        # Negative integer y
        with self.assertRaises(ValueError):
            Rectangle(10, 20, 5, -6)
    
    def test_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r2.area(), 56)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display(self, mock_stdout):
        r1 = Rectangle(3, 2)
        expected_output = "###\n###\n"
        r1.display()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

        # Clear mock_stdout for the next case
        mock_stdout.truncate(0)
        mock_stdout.seek(0)
        
        r2 = Rectangle(2, 3, 2, 2)
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        r2.display()
        self.assertEqual(mock_stdout.getvalue(), expected_output)
    
    def test_str_method(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        expected_output = '[Rectangle] (12) 2/1 - 4/6'
        self.assertEqual(str(r1), expected_output)

        r2 = Rectangle(5, 5, 1)
        expected_output = f'[Rectangle] ({Rectangle._Base__nb_objects}) 1/0 - 5/5'
        self.assertEqual(str(r2), expected_output)

    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), f'[Rectangle] ({Rectangle._Base__nb_objects}) 10/10 - 10/10')

        r1.update(89)
        self.assertEqual(str(r1), '[Rectangle] (89) 10/10 - 10/10')

        r1.update(89, 2)
        self.assertEqual(str(r1), '[Rectangle] (89) 10/10 - 2/10')

        r1.update(89, 2, 3)
        self.assertEqual(str(r1), '[Rectangle] (89) 10/10 - 2/3')

        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), '[Rectangle] (89) 4/10 - 2/3')

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), '[Rectangle] (89) 4/5 - 2/3')

    def test_update_kwargs(self):
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), f'[Rectangle] ({Rectangle._Base__nb_objects}) 10/10 - 10/10')

        r1.update(height=1)
        self.assertEqual(str(r1), f'[Rectangle] ({Rectangle._Base__nb_objects}) 10/10 - 10/1')

        r1.update(width=1, x=2)
        self.assertEqual(str(r1), f'[Rectangle] ({Rectangle._Base__nb_objects}) 2/10 - 1/1')

        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), '[Rectangle] (89) 3/1 - 2/1')

        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), '[Rectangle] (89) 1/3 - 4/2')

    def test_to_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9, 1)
        expected_dict = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertIsInstance(r1.to_dictionary(), dict)
        self.assertDictEqual(r1.to_dictionary(), expected_dict)

    def test_update_from_dict(self):
        r1 = Rectangle(10, 2, 1, 9, 1)
        self.assertEqual(str(r1), "[Rectangle] (1) 1/9 - 10/2")
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertNotEqual(r1, r2)

    def test_to_json_string(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertIsInstance(dictionary, dict)
        self.assertEqual(dictionary, {'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8})
        self.assertIsInstance(json_dictionary, str)
        self.assertEqual(json_dictionary, '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]')


if __name__ == '__main__':
    unittest.main()