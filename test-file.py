import unittest
import file1


class Test_File1(unittest.TestCase):

    def test_locate_city(self):
        self.assertEqual(file1.locate_city('Chicago'), 'Illinois')
        self.assertEqual(file1.locate_city('Austin'), 'Texas')
        self.assertEqual(file1.locate_city('San Diego'),
                         'That city does not exist.')


if __name__ == '__main__':
    unittest.main()
