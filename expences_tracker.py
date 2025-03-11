from datetime import datetime
import os
#Access the file
file="expences.txt"

print("____Welcome to our Expence tracker application____\n")

money=int(input("Enter your  total amount:"))
#Using while loop for show the manu

while True:
    print("1 Enter your amount to the list.")
    print("2. Show the previous Expence.")
    print("3. exit")
    print("4. Remove all data from the list.")

    choose=(input("Enter your option between(1-4):"))
    

    #Using Condisational function

    if choose=="1":
        add=input("Enter your item name:")
        amount=int(input("Enter the amount of the item:"))
        time=datetime.now().strftime("%d-%m-%Y %H-%M-%S")
        choose1=int(choose)

        
        entery=f"{add}:{amount} {time}"
        with open("expences.txt", "a") as f:
            f.write(entery)
            print("Your item is succesfully add to your list")
            f.close()
    elif choose=="2":
        remain= money - amount
        
        with open("expences.txt","r") as f:
            show=f.read()


            if show.strip():
                print("Your list of item\n")
                print(show)
                print(f"Your Remaning amount is:{remain}")
            else:
                print("Your list is empty")
            f.close()
    elif choose=="3":
        print("Thanl you for using our Expence tracking application")
        break
    elif choose=="4":
        with open("expences.txt","w") as f:
            pass
        
            f.close()
    else:
        print("Enter a valid option")





