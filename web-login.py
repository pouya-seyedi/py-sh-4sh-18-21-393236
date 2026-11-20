




#while True:
#    user=input("username:")
#    password=input("password:")
#    
#    while True:
#        if user =="" or user==" " or user=="  ":
#            print("username ro bezan:")
#            break
#        if user.isalnum()==True:
#            if user=="pouya":
#                print("user correct")
#                           
#        if password=="" or password==" " or password=="  ":
#            print("passeto bezan:")
#            break
#        if password.isdigit()==True :
#
#            if password=="1234":
#                print("password correct")
#            break    
#    break        
                






while True:
    user = input("username: ")
    password = input("password: ")

    user_correct = False
    password_correct = False

    
    if user == "" or user == " ":
        print("username ro dorost vared kon")

    elif user.isalnum() == False:
        print("username faghat horoof va ya adad bashe")

    elif user == "pouya":
        print("username correct")
        user_correct = True

    else:
        print("username incorrect")


    if password == "" or password == " ":
        print("password ro dorost vared kon")

    elif password.isdigit() == False:
        print("password bayad adad bashd")

    elif password == "1234":
        print("password correct")
        password_correct = True

    else:
        print("password incorrect")

    
    if user_correct == True and password_correct == True:
        print("login successful")
        break


    elif user_correct == True and password_correct == False:

        while password_correct == False:
            password = input("password: ")

            if password == "" or password == " ":
                print("password ro dorost vared kon")

            elif password.isdigit() == False:
                print("password bayad adad bashad")

            elif password == "1234":
                print("password correct")
                password_correct = True

            else:
                print("password incorrect")

        print("login successful")
        break

     
    elif user_correct == False and password_correct == True:

        while user_correct == False:
            user = input("username: ")

            if user == "" or user == " ":
                print("username is empty")

            elif user.isalnum() == False:
                print("username bayad hroof ya adad bashad")

            elif user == "pouya":
                print("username correct")
                user_correct = True

            else:
                print("username incorrect")

        print("login successful")
        break

    
    else:
        print("both incorrect")
        print("try again")




            

        

    