import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):
    def test1(self):
        """checks is empy string returns false"""
        pwd = ''
        expectedPWD = False
        self.assertEqual(check_pwd(pwd), expectedPWD)

    def test2(self):
        """checks if string len 7 fails, returns false"""
        pwd = 'aaaaaaa'
        expectedPWD = False
        self.assertEqual(check_pwd(pwd), expectedPWD)

    def test3(self):
        """checks if len string 21 fails, returns false"""
        pwd = 'aaaaaaaaaaaaaaaaaaaaa'
        expextedPWD = False
        self.assertEqual(check_pwd(pwd), expextedPWD)

    def test4(self):
        """checks if len string 42 fails, returns false"""
        pwd = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        expextedPWD = False
        self.assertEqual(check_pwd(pwd), expextedPWD)


if __name__ == '__main__':
    unittest.main()
