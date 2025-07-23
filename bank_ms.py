usernames = ["Faiq", "Ali", "Zain", "Hadi", "Ibrahim", "Faizan", "Moiz"]
passwords = ["Faiq1234", "Ali12345", "Zain1234", "Hadi12345", "Ibrahim123", "Faizan123", "Moiz1234"]
account_numbers = [11111111, 22222222, 33333333, 44444444, 55555555, 6666666, 7777777]
account_balances = [1000,2000,3000,4000,5000,6000,7000]


print("\nWelcome to Bank Alfalah Official Website")
print("\n1: Create a New Account")
print("\n2: Already have an existing account, Select to Login")



login_or_signup_input = input("Enter Your Choice : (1 or 2)")
if login_or_signup_input == "1":
    name_input1 = input("Enter Your First Name :")
    name_input2 = input("Enter Your Last Name :")  
    
    def check_password_strength(password):
        if len(password) < 8:
            return "Weak: Password should contain at least 8 characters"
        if not any(char.isdigit() for char in password):
            return "Weak: Password should contain at least one digit"
        if not any(char.isupper() for char in password):
            return "Weak: Password should contain at least one uppercase letter"
        return "Strong Password!"

    while True:
        password_input = input('Create a New Password: ')
        strength_result = check_password_strength(password_input)
        if strength_result == "Strong Password!":
            break
        print(strength_result)
    
    
    cnic_input = input('Enter Your CNIC Number : ')        
                                             
if len(cnic_input) != 13:
        print("Invalid CNIC Number")
else:
        phone_number_input = input('Enter Your Phone Number :')
        if len(phone_number_input) != 11:
            print("Invalid Phone Number")
        else:
         email_input = input("Enter Your Email Address :")
         print("Account Creation Successfull!")
        #  update_username_info = name_input1 + name_input2
        #  update_login_info = usernames.add(update_username_info)
        #  update_password_info = passwords.add(password_input)
         
         

if login_or_signup_input == "2":
    username_input = input("\nEnter Your Username :")
    user_password_input = input("\nEnter Your Password :")
    if username_input in usernames:
        index = usernames.index(username_input)
        if user_password_input == passwords[index]:
            print("Login Successfull !")
            
            balance_inquiry = print("1: Balance inquiry")
            transfer_money = print("2: Transfer Money")
            
            
            
            
            
                     
         
         
        
         
                
    
    
            
    
            
    
    

   



