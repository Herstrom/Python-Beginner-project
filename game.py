from datetime import datetime
#i am creating a Diary for my dealy task

file="book.txt"
with open("book.txt","w") as f:
    f.write()
print("_______WELCOME TO OUR DIARY_______")
while True:
    print("Choose your option:-\n")
    print("1.Add new task in diary.")
    print("2.Show the existing task.")
    print("3.Exit")

    choose=input("Enter a option between(1-3):")

    if choose=="1":
        entery=input("Enter your task for diary:")
        time=datetime.now().strftime("%d-%m-%Y %H-%M-%S")
        fullentery=(f"{time} {entery}")
        
           #Acessing the file 
        with open("book.txt","a") as f:
            f.write(fullentery)
            print("your task is add sucessfuly")
    elif choose=="2":
        with open("book.txt","r") as f:

            content=f.read()
        #Check the file is Empty or Not
        if content.strip():
            print("your task\n")
            print(content)
        else:
            print("ypur diary is empety")
    elif choose=="3":
        print("Good bye!")
        break
    else:
        print("Choose a valid options!")









