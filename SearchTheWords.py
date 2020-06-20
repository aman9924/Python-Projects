import datetime

lst=[]
length=0
def add():
    global temp
    temp=0
    for x in range(length):
        temp = temp + lst[x]
    return temp
def sub():
    global x
    global y
    try:
        x,y=lst
        return x-y
    except Exception as e:
        return "Sorry I cannot subtract more than two numbers"
def mul():
    global m
    m=1
    for x in range(length):
        x=x * lst[x]
    return m
def div():
    a,b=lst
    return a/b
def modulo():
    a,b=lst
    return a%b
def mini():
    return min(lst)
def maximum():
    return max(lst)
# def LCM():
#     global i
#     large = maximum()
#     for i in range(large, mul() + 1, large):
#         for j in range(length):
#             if (length - 1 == j):
#                 if (i % lst[j] == 0):
#                     return (i)
#             if (i % lst[j] == 0):
#                 pass
#             else:
#                 break
#     print(i)
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good morning Aman")
    elif hour >= 12 and hour < 16:
        print("Good Afternoon Aman")
    else:
        print("Good Evening Aman")
    print("Hello Aman I am your smart calculator, how can I help you")

def name():
    print("I am your smart calculator")

def take_command():
    try:
        globals() ['lst'] = []
        print("Enter the task: ")
        query = input()
        for words in query.split(' '):
            if words.isdigit():
                lst.append(eval(words))
        globals()['length'] = len(lst)
    except Exception as e:
        print("Please provide the input again.")
        return "None"
    return query




if __name__ == "__main__":
    wish()
    while (True):
        query = take_command().lower()
        if ("add" in query or "plus" in query or "addition" in query or "+" in query):
            print("Addition of given number is ",add())
        elif ("divide" in query or "divison" in query or "/" in query):
            print("Divison of given number is ",div())
        elif ("multiply" in query or "into" in query or "multiplication" in query or "product" in query or "x" in query):
            print("Multiplication of given number is  ",mul())
        elif ("subtract" in query or "minus" in query or "subtraction" in query or "-" in query):
            print("Subtraction of given number is ",sub())
        elif ("min" in query or "minimun" in query or "smallest" in query):
            print("The smallest number in the given list is ",mini())
        elif ("max" in query or "maximum" in query or "largest" in query):
            print("The largest number in the given list is ",maximum())
        elif 'who' in query:
            name()
        elif 'exit' in query or 'quit' in query or 'cancel process' in query:
            print("Thanks For Using Me...\nSee you Again")
            quit()
