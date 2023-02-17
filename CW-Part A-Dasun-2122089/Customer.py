#importing libraries
import pandas as pd 

#process of customer
def customer():
    #making loop a to user so user can select until user finish proccess
    while True:
        
        #Options
        print("\nOption 1 : View car info")
        print("Option 2 : Any specific Milage or Price")
        print("Option 3 : Make an appointment")
        print("Option 4 : Check the appointment if its confirm or not")
        print("Option 5 : Exit the Program" )

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
                

        #opening the car details file
        if  user_input == 1:
            data = pd.read_csv("CarDetails.txt")
            #user can only view availabale cars
            view = (data['Sold']== 'no')
            #user can't see the asking price
            print(data.loc[view,['ModelNo','Model','Milage(km)','Year','Owner','Price(Mil)']])

        #customer sorting data    
        if user_input == 2 :
            #user inserting whether it is milage or price
            user = int(input("Enter whether is Milage or Price \nIf its Milage please enter number 1 or if its price please enter number 2: "))
            if user == 1:
                
                #sorting data for milage
                data = pd.read_csv("CarDetails.txt")
                num = int(input("Enter your milage (KM): "))
                mil = (data['Milage(km)']<= num)
                print(data.loc[mil,['ModelNo','Model','Milage(km)','Year','Owner','Price(Mil)']])

            if user == 2:
                #sorting data for price
                data = pd.read_csv("CarDetails.txt")
                num = float(input("Enter your price(Rs.Mil): "))
                pri = (data['Price(Mil)']<= num)
                print(data.loc[pri,['ModelNo','Model','Milage(km)','Year','Owner','Price(Mil)']])
        
       

        

        #Requesting Appointments
        if user_input == 3:
            #Entering details of customer to make an appointment
            file = open("Appointments.txt","r")
            #user inputs
            appo_num = len(file.readlines())
            name = input("Enter the car customer name: ")
            car = input("Enter the model number that you want to try a testdrive: ")
            date = input("Enter the appointmant date(DD/MM/YY): ")
            time = input("Enter the appointment time(AM/PM): ")
            status = 'Pending'

            #making a list for appointment
            listApp=[]
            listApp.append(str(appo_num))
            listApp.append(name)
            listApp.append (str(car))
            listApp.append (str(date))
            listApp.append (str(time))
            listApp.append(status)

            #joining all user inputs
            details=",".join(listApp)
 
            #appending the appointment to the appoinment file
            fo = open("Appointments.txt","a")
            fo.write("\n")
            fo.write(details)
            print("Appointment added successfully")
            fo.close()
           
        #checking appointments status
        if user_input == 4:
            appo_confirm = pd.read_csv("Appointments.txt",index_col='AppointmantNo')
            #user can only see confirmed appointments
            view = (appo_confirm['Status']== 'Confirmed')
            print(appo_confirm.loc[view])
        
            
        #ending the loop
        if user_input >= 5:
            print("Thank you!!! Come Again!")
            break 

            

#log in proccess of customer
def login():
    #Creating variables
    fo = 0
    username = 0
    password = 0
    #Opening the customer login details file
    fo = open("CustomerLoginDetails.txt","r")
    
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
                        customer()
            except:
                print("Incorrect password or username")
    except:
        print("Username or password doesn't exist")
        
    fo.close()
    



