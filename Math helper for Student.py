import random

def show_Display(number_01,number_02,answer,op):
    display = "{D1} {D2} {D3} {D4}\n".format(D1 = number_01 , D2 = op , D3 = number_02 , D4 = "=")
    print(display)
    for i in range(0,3):
        Entered_Number = float(input("Enter Number : "))
        if(answer == Entered_Number):
            print("Correct!!!")
            break
        else:
            if(i == 2):
                print("<-- All Answers are Incorrect [Answer:{A1}] --> ".format(A1=answer))
            else:
                print("Try Again!!!\n")
    
    return 0

def add():
    answer = number_01 + number_02
    show_Display(number_01,number_02,answer,"+")
    return 0

def subtract():
    answer = number_01 - number_02
    show_Display(number_01,number_02,answer,"-")
    return 0

def Multiply():
    answer = number_01 * number_02
    show_Display(number_01,number_02,answer,"*")
    return 0

def Divide():
    answer = (number_01 / number_02)
    answer = "{:.2f}".format(answer)
    show_Display(number_01,number_02,float(answer),"/")
    return 0

def Power():
    answer = (number_01//10) ** (number_02//10)
    show_Display((number_01//10),(number_02//10),answer,"^")
    return 0


def select_OP(choice):

    if(choice == '#'):
        return -1
    elif(choice in ('+','-','*','/','^')):
        if(choice == "+"):
            add()
        elif(choice == "-"):
            subtract()
        elif(choice == "*"):
            Multiply()
        elif(choice == "/"):
            Divide()
        elif(choice == "^"):
            Power()
        else:
            print("<-- Reset -->\n")



while(True):
    number_01 = random.randint(1, 100)
    number_02 = random.randint(1, 100)

    print("----------------------------------------------------------------")
    print("  Add[+]  Subtract[-]  Multiply[*]  Divide[/]  Power[^] Exit[#]")
    print("----------------------------------------------------------------\n")
    
    choice = str(input("Enter Operator :"))
    if (select_OP(choice) == -1):
        print("Done . Terminating")
        exit()