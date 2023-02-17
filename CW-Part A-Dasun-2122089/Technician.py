#importing libraries
import pandas as pd
#proccess of technicain
def technician():
    while True:
        
        #Options
        print("\nOption 1 : View previous maintaince")
        print("Option 2 : Enter new maintaince")
        print("Option 3 : Exit the Program" )
        

        #user input
        u_inp = True
        user_input = 0
        #when user insert a string and giving another chance until user insert an integer value
        while u_inp == True:
            #showing the error to user
            try:
                user_input = int(input("Select an option (please input the relevent number) :"))
                u_inp = False
            except ValueError:
                print("Only integers are allowed") 

        #Opening maintain file
        if user_input == 1:
            main = pd.read_csv("Maintain.txt")
            pd.set_option('display.max_columns',7)
            print(main)


        #adding maintain details
        if user_input == 2:
            module_num = input("Enter the module number: ")
            module = input("Enter the module name: ")
            name = input("Enter the customer name: ")
            date = input("Enter the maintained date: ")
            time = input("Enter the maintained time: ")
            des = input("Enter the maintain description: ")
            cost = input("Enter the maintained cost: ")
            
            #making a list for maintain details
            listMain=[]
            listMain.append(str(module_num))
            listMain.append(module)
            listMain.append (str(name))
            listMain.append (str(date))
            listMain.append (str(time))
            listMain.append (str(des))
            listMain.append (str(cost))
            

            details=",".join(listMain)
            

            fo = open("Maintain.txt","a")
            fo.write("\n")
            fo.write(details)
            print("Maintain added successfully")
            fo.close()

        #breaking the loop
        if user_input >= 3:
            print("Thank you!!! Come Again!")
            break


#log in proccess of customer
def login():
    #Creating variables
    fo = 0
    username = 0
    password = 0
    #Opening the customer login details file
    fo = open("technicianLoginDetails.txt","r")
    
    #inputting the username and password
    
    username = input("Enter your username: ")
    password = input("Enter your password: ")
        
    #making empty lists
    user = []
    passw = []
    #reading the file line by line
    for i in fo:
        #spliting the selected line
        a,b = i.split(",")
        #removing any leading spaces and trailing characters
        b = b.strip()
        #appending the username and password to the list
        user.append(a)
        passw.append(b)
    #Create a dictionary to a appended word in list and join it together
    data = dict(zip(user,passw))
        
        
    #checking the user input username whether is in dictionary
    try:
        if data[username]:
            try:
                #checking the password and the relevant username is equal or not          
                if password == data[username]:
                        print("\nLogin success")
                        print("Hi,",username,"Welcome to Asian car sale")
                        #calling the customer features function
                        technician()
            except:
                print("Incorrect password or username")
    except:
        print("Username or password doesn't exist")
        
    fo.close()      

