import Database_Model as dbHandler
import re

class Login_Application:

    def validate_username(self,usrname):
        result = False if next((chr for chr in usrname if chr.isdigit()), None) else True
        return result
    
    def validate_for_minimum_length_of_password(self,password):
            flag = 0
            if (len(password)<=6): 
                flag = -1
            elif not re.search("[a-z]", password): 
                flag = -1
            elif not re.search("[A-Z]", password): 
                flag = -1
            elif not re.search("[0-9]", password): 
                flag = -1
            else: 
                flag = 0
                return True 
            if flag ==-1: 
                return False   

    def create_user(self,username, password):

            validate_only_letteres_allowed_in_username = Login_Application.validate_username(self,username)

            validate_for_minimum_length_of_password=Login_Application.validate_for_minimum_length_of_password(self,password)
            
            if validate_only_letteres_allowed_in_username==False:
                print("Only letteres are allowed in username!")

            elif(validate_for_minimum_length_of_password==False):
                print("Password length 6, Password should consist of at least 1 alphabet, Password should consist of at least 1 integer !")
            
            else:
                result=dbHandler.insertUser(username, password)
                print("user creation successful!")
                return result

    def check_login(self,username, password):

            check_for_success_login = dbHandler.check_login(username,password)

            if check_for_success_login==False:
                 print("Login failed!")
            else:
                print("Login Success!")
                return check_for_success_login