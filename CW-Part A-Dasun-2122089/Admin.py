#importing libraries
import pandas as pd 
#process of admin
def admin():
    while True:
    
        #Options
        print("\nOption 1 : View car info")
        print("Option 2 : Adding a new car to car info")
        print("Option 3 : Editing car info in car details file")
        print("Option 4 : Editing car info if it's sold")
        print("Option 5 : View Customer info")
        print("Option 6 : Check Appointments" )
        print("Option 7 : editing appointments")
        print("Option 8 : Exit form program")
    

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
        #Opening the car details file
        if user_input == 1:
            data = pd.read_csv("CarDetails.txt" )
            
            print(data)
            
        #admin add a new details file
        if user_input == 2:
            #admin adding the details into the car details file
            
            module_no = input("Enter the car model number: ")
            module = input("Enter the car model: ")
            milage = int(input("Enter the milage(km): "))
            year = input("Enter the year of the car: ")
            owner = input("Enter the owner details(1st/2nd/3rd/...): ")
            selling_price = float(input("Enter the selling price of the car(Million): "))
            asking_price = float(input("Enter the asking price of the car(Million): "))
            sold = 'no'

            #making a list for car details
            listCar=[]
            
            
            listCar.append(module_no)
            listCar.append(module)
            listCar.append (str(milage))
            listCar.append (str(year))
            listCar.append(owner)
            listCar.append (str(selling_price))
            listCar.append (str(asking_price))
            listCar.append(sold)

            #joining all user inputs
            details=",".join(listCar)
            
            #appending data to the car details file
            fo = open("CarDetails.txt","a")
            fo.write("\n")
            fo.write(details)
            print("New detail added successfully")
            fo.close()



        #changing existing data    
        if user_input == 3:
            data = pd.read_csv("CarDetails.txt")
            print(data)
            while True:
                end_loop = int(input("Enter '1' to start the operation \nOr Enter number '2' to stop the operation: "))
                if end_loop == 1:
                    with open ('CarDetails.txt','r') as file:
                        user = int(input("Enter the line number number: "))
                        #reading the selected line
                        content = file.readlines()
                        find = content[user + 1]
                        # Replace the target string
                        check_word = input("Enter the word that you want to chanege: ")
                        change_word = input("Enter the word that you want to add: ")
                        find = find.replace(check_word, change_word)
                        content[user + 1] = find
                        # Write the file out again
                        with open ('CarDetails.txt','w') as file:
                            file.writelines(content)
                            print(find)
        
                if end_loop == 2:
                    break

            
        #changing sold status
        if user_input == 4:
            data = pd.read_csv("CarDetails.txt")
            #user can only see available cars
            view = (data['Sold']== 'no')
            print(data.loc[view])
            with open ('CarDetails.txt','r') as file:
    
                user = int(input("Enter the line number number: "))
                #reading the selected line
                content = file.readlines()
                find = content[user + 1]
                

                # Replace the target string
                find = find.replace('no', 'yes')
                content[user + 1] = find
                
    
            # Write the file out again
            with open ('CarDetails.txt','w') as file:
                file.writelines(content)
                print(find)


        #Opening customer details
        if user_input == 5:
            customer_data = pd.read_csv("CustomerDetails.txt")
            print(customer_data)
        #Check appointments 
        if user_input == 6:
            details = pd.read_csv("Appointments.txt",index_col='AppointmantNo')
            print(details)

    

        #editing appointments status
    
        if user_input == 7:
            details = pd.read_csv("Appointments.txt",index_col='AppointmantNo')
            view = (details['Status']== 'Pending')
            print(details.loc[view])
            with open ('Appointments.txt','r') as file:
                
                user = int(input("Enter the Appointment number : "))
                #reading selected line
                content = file.readlines()
                find = content[user]
                

                # Replace the target string
                find = find.replace('Pending', 'Confirmed')
                content[user] = find
                
                
            # Write the file out again
            with open ('Appointments.txt','w') as file:
                file.writelines(content)
                print(find)
        #breaking the loop
        if user_input >= 8:
            print("Thank you!!! Come Again!")
            break
            

#log in proccess of customer
def login():
    #Creating variables
    fo = 0
    username = 0
    password = 0
    #Opening the customer login details file
    fo = open("AdminLoginDetails.txt","r")
    
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
                        admin()
            except:
                print("Incorrect password or username")
    except:
        print("Username or password doesn't exist")
        
    fo.close()
    



