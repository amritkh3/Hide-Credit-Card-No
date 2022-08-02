"""hiding the credit card no
write  a program where user will enter their credit cards number and it will return
all the nubers hiding except last four digits
1.ask user to anput their cerdit card number and assign it ti the variable cardno.
2.declare a variable visibleno and assign it with a value cardno[-4:]which will be the last 4 num 
of credit card no entered.
declare a empty variable  hide
3.loop through all the index of credit no excepth the last four digit.
4.print"*"after every loop and assign it to the variable hide .
5.print hide+visibleno

"""


cardno=input("enter your 10 digit card number ")
visibleno=cardno[-4:]
hide=""
for index in range(len(cardno)-4):
    hide=hide+"*"


print(hide+visibleno)