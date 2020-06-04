def getdate():
    import datetime
    return datetime.datetime.now()
# time= getdate()
# print(time)



def lock(k):
    if (k == 1):
        p = int(input("Enter 1-Exercise      2-Food:- "))
        if (p == 1):
            value = input("Enter The Exercise:- ")
            with open("Aman-Exercise.txt", "a") as op:
                time = getdate()
                op.write(str(time) + " - " + value+"\n")
            print("Your Response Has Been Entered")
        elif (p == 2):
            value = input("Enter The Food:- ")
            with open("Aman-Food.txt", "a") as op:
                time = getdate()
                op.write(str(time) + " - " + value+"\n")
            print("Your Response Has Been Entered")
        else:
            print("Enter Correct Option")
    elif (k == 2):
        p = int(input("Enter 1-Exercise      2-Food:- "))
        if (p == 1):
            value = input("Enter The Exercise:- ")
            with open("Amar-Exercise.txt", "a") as op:
                time = getdate()
                op.write(str(time) + " - " + value)
            print("Your Response Has Been Entered")
        elif (p == 2):
            value = input("Enter The Food:- ")
            with open("Amar-Food.txt", "a") as op:
                time = getdate()
                op.write(str(time) + " - " + value)
            print("Your Response Has Been Entered")
        else:
            print("Enter Correct Option")
    elif (k == 3):
        p = int(input("Enter 1-Exercise      2-Food:- "))
        if (p == 1):
            value = input("Enter The Exercise:- ")
            with open("Golu-Exercise.txt", "a") as op:
                time = getdate()
                op.write(str(time) + " - " + value)
            print("Your Response Has Been Entered")
        elif (p == 2):
            value = input("Enter The Food:- ")
            with open("Golu-Food.txt", "a") as op:
                time=getdate()
                op.write(str(time) + " - " + value)
            print("Your Response Has Been Entered")
        else:
            print("Enter Correct Option")


def retrieve(k):
    if (k == 1):
        p = int(input("Enter 1-Exercise      2-Food:- "))
        if (p == 1):
            # value = input("Enter The Exercise:- ")
            with open("Aman-Exercise.txt") as op:
                for text in op:
                    print(text)
        elif (p == 2):

            with open("Aman-Food.txt") as op:
                for text in op:
                    print(text)

        else:
            print("Enter Correct Option")
    elif (k == 2):
        p = int(input("Enter 1-Exercise      2-Food:- "))
        if (p == 1):
            # value = input("Enter The Exercise:- ")
            with open("Amar-Exercise.txt") as op:
                for text in op:
                    print(text)
        elif (p == 2):

            with open("Amar-Food.txt") as op:
                for text in op:
                    print(text)

        else:
            print("Enter Correct Option")

    elif (k == 3):
        p = int(input("Enter 1-Exercise      2-Food:- "))
        if (p == 1):
            # value = input("Enter The Exercise:- ")
            with open("Golu-Exercise.txt") as op:
                for text in op:
                    print(text)
        elif (p == 2):

            with open("Golu-Food.txt") as op:
                for text in op:
                    print(text)

        else:
            print("Enter Correct Option")

def again():
    a=int(input("Enter 1 for Retirive or 2 to lock:- "))
    if(a==1):
        b=int(input("Enter 1-Aman 2-Amar 3-Golu:- "))
        retrieve(b)
    else:
        b=int(input("Enter 1-Aman 2-Amar 3-Golu:- "))
        lock(b)
while(True):
    ans = input("Do you Want to Continue: Type y-Yes or n-No:- ")
    if(ans=='y'):
        again()
    elif(ans=='n'):
        break
    else:
        print("Enter Correct Response")








