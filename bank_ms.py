usernames = ["Faiq", "Ali", "Zain", "Hadi", "Ibrahim", "Faizan", "Moiz"]
passwords = ["Faiq1234", "Ali12345", "Zain1234", "Hadi12345", "Ibrahim123", "Faizan123", "Moiz1234"]
account_numbers = [11111111, 22222222, 33333333, 44444444, 55555555, 6666666, 7777777]
account_balances = [100000,200000,300000,400000,500000,600000,700000]



print("Welcome to Bank Alfalah Official Mobile App")
print("\n1: Create a New Account")
print("2: Already have an existing account, Select to Login")

login_or_signup_input = input("Enter Your Choice (1 or 2): ")

if login_or_signup_input == "1":
    name_input1 = input("Enter Your First Name: ")
    name_input2 = input("Enter Your Last Name: ")

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

    while True:
        cnic_input = input("Enter Your CNIC Number (without dashes): ")
        if len(cnic_input) != 13 or not cnic_input.isdigit():
            print("Invalid CNIC Number - must be 13 digits")
        else:
            break

    while True:
        phone_number_input = input("Enter Your Phone Number: ")
        if len(phone_number_input) != 11 or not phone_number_input.isdigit():
            print("Invalid Phone Number - must be 11 digits")
        else:
            break

    email_input = input("Enter Your Email Address: ")
    print("Account Creation Successful!!")
    full_name = name_input1 + "_" + name_input2
    usernames.append(full_name)
    passwords.append(password_input)

        
         
         

if login_or_signup_input == "2":
    username_input = input("\nEnter Your Username :")
    user_password_input = input("\nEnter Your Password :")
    if username_input in usernames:
        index = usernames.index(username_input)
        if user_password_input == passwords[index]:
            print("Login Successfull !")
            print(f"Welcome {username_input} ")
            
            balance_inquiry = print("1: Balance inquiry")
            transfer_money = print("2: Transfer Money")
            deposit_money = print("3: Money Deposit")
            transaction_choice = input("Enter Your Choice (1-3)")
            if transaction_choice == "1":
                
                print(f"{username_input}, Your Account Balance is {account_balances[index]}")
            elif transaction_choice == "2":
                transfer_input = input("Enter the account number of the account you want to transfer money to:")
                transfer_amount = int(input("Enter the amount you want to transfer: "))
                if transfer_amount > (account_balances[index]):
                 print("Insufficient Balance")
                else:
                    account_balances[index] -= transfer_amount
                print(f"Transaction Successful! Your Remaining Balance is {account_balances[index]}")

                 
                
                
                
                
                
            
                
            
            
            
            
            
            
            
            
            
                     
         
         
        
         
                
    
    
            
    
            
    
    

   



