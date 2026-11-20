



while True:
 
 while True:
      name=input("esm:")
      
      
      if name=="" or name==" " or name=="  ":
          print("name ro vared kon")
          continue
      if name.isalpha()==True:
          if name.isprintable()==True:
              if name.islower()==False:
                  print("ba horof kochik bezan")
                  continue
              if name.islower()==True:
                  name=name.islower()
                  print(name)
                  break
      else:
          print("esm na motabar")
          continue
      
 while True:
   phone=input("telephon:")
   while True:
       if phone=="" or phone==" " or phone=="  ":
           print("telephon vared kon:")
           break
       if len (phone)== 11 and phone.startswith("09")==True and phone.isdigit()==True:
           print("shomareh sabt shod")
           break
       else:
           print("shomareh eshtebah")
           break
   while True:
     address=input("address:")
     while True:
         if address =="" or address==" " or address=="  ":
             print("address vared kon:")
             continue
         if address.isalpha()==True and address.isprintable()==True:
             print("address saabt shod:")
             break
         else:
             print("address eshtebah:")
             break
     while True:
      email=input("email:")
      while True:
          if email=="" or email==" " or email=="  ":
              print("email vared kon:")
              continue
          if email.endswith("@gmail.com") and email.isalnum()==True:
              print("email sabt shod:")
              break
          else:
              print("email eshtebah:")

              continue
      while True:
       codepost=input("code posti:")
       while True:
           if codepost=="" or codepost==" " or codepost=="  ":
               print("code posti vared kon:")
               break
           if len (codepost)==10 and codepost.isdigit()==True:  
                print("code posti sabt shod:")
                break
           else:
               print("code posti na motabar:") 
               continue
       while True:
           codemelli=input("code melli:")
           while True:
               if codemelli=="" or codemelli==" " or codemelli=="  ":
                   print("code melli ro vared kon:")
                   break
               if len(codemelli)==10 and codemelli.isdigit==True:
                   print("code melli sabt shod:")
                   break
               else:
                   print("code melli namotabar:")
                   break
                                              
 
                            


                   
                                 
                    
            