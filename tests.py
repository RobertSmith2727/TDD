import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):
    def test1(self):
        """checks is empy string returns false"""
        pwd = ''
        expectedPWD = False
        self.assertEqual(check_pwd(pwd), expectedPWD)


if __name__ == '__main__':
    unittest.main()
