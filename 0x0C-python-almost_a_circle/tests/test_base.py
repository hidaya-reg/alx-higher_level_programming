import unittest
from unittest.mock import mock_open, patch
from modeltest.rectangle import Rectangle
from modeltest.base import Base

class TestBase(unittest.TestCase):

    def setUp(self):
        Base.__nb_objects = 0

    def test_id_not_provided(self):
        b1 = Base()
        b2 = Base()

        self.assertEqual(b1.id + 1, b2.id)
    
    def test_id_provided(self):
        b = Base(25)
        self.assertEqual(b.id, 25)

    @patch('builtins.open', new_callable=mock_open)
    def test_save_to_file(self, mock_file):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(5, 5, 1, 0, 2)

        Rectangle.save_to_file([r1, r2])

        # Verify that the file was opened with the correct name
        mock_file.assert_called_once_with('Rectangle.json', 'w')
         # Prepare the expected output
        expected_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        expected_json = Base.to_json_string(expected_dicts)
        # Verify that the correct JSON string was written to the file
        mock_file().write.assert_called_once_with(expected_json)
    
    def test_from_json_string(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4}, 
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertIsInstance(list_output, list)
        self.assertEqual(list_output, list_input)

    def test_create(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertNotEqual(r1, r2)

    @patch('builtins.open', new_callable=mock_open)
    def test_load_from_file(self, mock_file):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(5, 5, 1, 0, 2)
        
        # Prepare the expected output for saving
        expected_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        expected_json = Base.to_json_string(expected_dicts)

        # Call save_to_file to create the file
        Rectangle.save_to_file([r1, r2])

        # Mock the file reading to return the expected JSON string
        mock_file.return_value.read.return_value = expected_json

        # Now test load_from_file
        loaded_rectangles = Rectangle.load_from_file()

        # Check that the loaded objects have the same attributes as the original ones
        self.assertEqual(str(r1), str(loaded_rectangles[0]))
        self.assertEqual(str(r2), str(loaded_rectangles[1]))

    @patch('builtins.open', new_callable=mock_open)
    def test_save_to_file_csv(self, mock_file):
        # Create some Rectangle instances
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        list_rectangles_input = [r1, r2]

        # Call the method to test
        Rectangle.save_to_file_csv(list_rectangles_input)

        # Check that the file was opened with the correct filename
        mock_file.assert_called_once_with('Rectangle.csv', 'w', newline='')

        # Get the handle to the mock file
        handle = mock_file()

        # Prepare the expected output
        expected_rows = [
        '1,10,7,2,8\r\n',  # String representation of values from r1.to_dictionary()
        '2,2,4,0,0\r\n'    # String representation of values from r2.to_dictionary()
    ]

       # Verify that the correct strings were written to the file
        # This checks for the exact strings that were written
        handle.write.assert_any_call(expected_rows[0])
        handle.write.assert_any_call(expected_rows[1])




if __name__ == 'main':
    unittest.main()


        