
print("https://github.com/CodeCamper999/SaveInfo/tree/main")

print("visit github README")

print("Also the program will start over endless times until it reaches the number of times you put or you input -Brk")

BreakCode = {
    "-Brk": "Turning Loop off",
}

TempSaves = []

NumberOfLoops = int(input("How many times do you want to loop: "))

CreateNewUsrname = input("Would you like to save a username or Temporary save a usr[S/T]:")


def CreateUser(usr):
    i = 1
    
    while i <= NumberOfLoops:
            
        i += 1
        print(NumberOfLoops)
        print(i)
        
        
        
        
        if usr == "S" or usr == "s":
            getusr = input("What is the username/password you would like to save(Put , if you want to see them better when printed exp: ,Cookies): ")
            if getusr == "-Brk" in BreakCode:
                break
            print("SA lets you see all users that are saved.")
            SeeNewUsr = input("Would you like to see new saved user[Y/N/SA]: ")
            CreateFile = open("SavedUsrNames.txt", "a+")
            CreateFile.write(getusr)
            CreateFile.close()
            
            if SeeNewUsr == "Y" or SeeNewUsr == "y":
                print(getusr)
            elif SeeNewUsr == "SA" or SeeNewUsr == "sa":
                with open("SavedUsrNames.txt", "r") as f:
                    filenames = f.read()
                    print(filenames)
                    f.close()
            
                
        elif usr == "T" or usr == "t":
            getTempusr = input("What is the username/password you would like to store temporarly: ")
            if getTempusr == "-Brk" in BreakCode:
                break
            
            TempSaves.append(getTempusr)
            print("SA allows you to see all names")
            SeeUsrName = input("Do you want to see the username/password[Y/N/SA]: ")
            
            if SeeUsrName == "Y" or SeeUsrName == "y":
                print(TempSaves[-1])
            elif SeeUsrName == "SA":
                print(TempSaves[0:])
            else:
                print("Starting Over...")
        else:
            print("Error please choose S/T")
            
            
CreateUser(CreateNewUsrname)

print("Done with program Python deletes all information that hasn't been saved...")
    
