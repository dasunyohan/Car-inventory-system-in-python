import Admin as admin
import Customer as customer
import Technician as technician
import Owner as owner

user_select = 0


user_select = int(input("\n1.Admin \n2.Customer \n3.Technicain \n4.Owner \nEnter the number that represent which user you are: "))

    
if user_select == 1:
    print("Now you are in Admin area. \nPlease enter your username and password to continue")
    admin.login()

if user_select == 2:
    print("Now you are in Customer area. \nplease enter your username and password to continue")
    customer.login()

if user_select == 3:
    print("Now you are in Technicain area. \nPlease enter your username and password to continue")
    technician.login()

if user_select == 4:
    print("Now you are in Owner area. \nPlease enter your username and password to continue")
    owner.login()

if user_select >= 5:
    print("Enter the relevant number")
        
