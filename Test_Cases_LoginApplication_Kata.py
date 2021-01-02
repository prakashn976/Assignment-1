import Models as dbHandler
import unittest
from LoginApplication_Kata import Login_Application

class Test_Login_App(unittest.TestCase):         

    def test_user_creation_positive(self):
        result=Login_Application.create_user(self,"prknagaraj","Prk123mouse")
        self.assertTrue(result)
    
    def test_user_creation_fail_only_letters_allowed_in_username(self):
        result=Login_Application.create_user(self,"akshaya1","akshaya123")
        self.assertFalse(result)

    def test_user_creation_fail_for_password_minimum_length(self):
        result=Login_Application.create_user(self,"guruguha","mabc")
        self.assertFalse(result)

    def test_user_creation_fail_Password_consist_of_at_least_1_alphabet(self):
        result=Login_Application.create_user(self,"skanda","123456")
        self.assertFalse(result)

    def test_user_creation_fail_Password_should_consist_of_at_least_1_integer(self):
        result=Login_Application.create_user(self,"battery","battery")
        self.assertFalse(result)   

    def test_user_login_positive(self):
        result=Login_Application.check_login(self,"prknagaraj","Prk123mouse")
        self.assertTrue(result)

    def test_user_login_negative(self):
        result=Login_Application.check_login(self,"prknagarajedd","Prk123mouseeee")
        self.assertFalse(result)
        

if __name__ == '__main__':
    unittest.main()