
"""
    This file consists of bank app function use for performing banj operations
"""

from getpass import getpass


data = {'1001' : ["simran", "passwd", 12000, '1601'], \
        '1002' : ["shahid", "admin", 10000, '2810'], \
        '1003' : ["rahul", "passpass", 13000, '0505'], \
        '1004' : ["tushar", "passwd", 12500, '1306']}

def bank_application(data, operation):
    
    """
        This function is for bank management of login and signup operation
        call the function ---> bank_application(data,opertaion)
        data --> dictionary type object
        operation --> string type object
    """
    
    if operation.lower() == "login":
        accno = input("\n Enter 4 digit number account number : ")
        if len(accno) == 4:
            if accno in data.keys():
                passwd = input("\n Enter password : ")
                if data[accno][1] == passwd:
                    print("\n Your details are : ")
                    #for i in data[acnno]:
                    print("*"*80)
                    print("\n Name : ", data[accno][0])
                    print("\n Accnount Number : ", accno)
                    print("\n Password : ", data[accno][1])
                    print("\n Balance : ", data[accno][2])
                    print("\n Your security answer : ", data[accno][3])
                    print("*"*80)
                        
                else:
                    print("\n Try again....Password does not matched....")
            else:
                print("\n No such accnount number...Please check")
        else:
            print("\n Invalid account number......")
            
    elif operation.lower() == "signup":
        name = input("\n Name : ")
        password = getpass("\n Password : ")
        security = input("\n Enter date of birth in form of ddmm : ")
        bal = eval(input("\n Enter your initial balance : "))
        accno = int(list(data.keys())[-1]) + 1  #generation new account number by getting the last number in keys
        data[accno] = [name, password, bal, security]
        print("\n Your account number is : ", accno)
        print("\n \n Thanks for sign up and We will deliver you best....")
        print("\n\n User the above account number for login.....")
    else:
        print("\n Operation not handled....")
        
bank_application(data, "login")
