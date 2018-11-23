import unittest
from gename import Gender


class GenderCase(unittest.TestCase):
    def test_speculate(self):
        gender = Gender()
        self.assertEqual(gender.speculate('Johanna'), 'F')
        self.assertEqual(gender.speculate('Mikko'), 'M')
        self.assertEqual(gender.speculate('abcdef'), 'U')


if __name__ == '__main__':
    unittest.main()
