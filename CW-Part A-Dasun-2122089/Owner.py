#importing libraries
import pandas as pd 

#process of owner
def owner():
    while True:
        #options
        print("\nOption 1 : View Top 5 Sold Car Models in each month")
        print("Option 2 : View number of cars sold in each month")
        print("Option 3 : View Monthly Profits")
        print("Option 4 : Exit the Program" )

        #user input
        u_inp = True
        user_input = 0
        while u_inp == True:
            try:
                user_input = int(input("Select an option (please input the relevent number) :"))
                u_inp = False
            except ValueError:
                print("Only integers are allowed")

        #viewing the top 5 cars
        if user_input == 1:
                data = pd.read_csv("Top5Cars.txt" )
                print(data)

        #opening the profit file in read mode
        if user_input == 2:
            file = open("NoOfCarsSold.txt",'r')
            #reading all lines
            content = file.readlines()
            #print Y axis
            print("\nY-axis/Month(2022)")
            print("    ^")
            #reading line by line
            for i in range(len(content)):
                #spliting months and profit
                month,profit = content[i].split(',')
                #removing any leading spaces and trailing characters
                profit = profit.strip()
                #convert profit str value to float and convert into integer value
                profit = int(float(profit))
                #rounding the profit
                profit = 5*round(profit/5)
                print(month,"| ",end='')
                #equaling the selcted line profit  
                for x in range (int((profit/5))):
                    print("*",end='')
                print()
            print("    0 --------------------> X-axis/No.of sold cars(* = average 5 cars)")         
            
                          
            file.close()


        #opening the profit file in read mode
        if user_input == 3:
            file = open("MonthlyProfit.txt",'r')
            #reading all lines
            content = file.readlines()
            #print Y axis
            print("\nY-axis/Month(2022)")
            print("    ^")
            #reading line by line
            for i in range(len(content)):
                #spliting months and profit
                month,profit = content[i].split(',')
                #removing any leading spaces and trailing characters
                profit = profit.strip()
                #convert profit str value to float and convert into integer value
                profit = int(float(profit))
                #rounding the profit
                profit = 5*round(profit/5)
                print(month,"| ",end='')
                #equaling the selcted line profit  
                for x in range (int((profit/5))):
                    print("*",end='')
                print()
            print("    0 --------------------> X-axis/Profit(* = average 5 Mil)")         
            
                          
            file.close()


        #ending the loop
        if user_input >= 4:
            print("Thank you!!! Come Again!")
            break 


#log in proccess of customer
def login():
    #Creating variables
    fo = 0
    username = 0
    password = 0
    #Opening the customer login details file
    fo = open("OwnerLoginDetails.txt","r")
    
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
                        owner()
            except:
                print("Incorrect password or username")
    except:
        print("Username or password doesn't exist")
        
    fo.close()



