from connector import *
from variables import *
from balpin import *

#journey

print("select \n 1 for virar \n 2 for bhayandar \n 3 for borivali ")
src=int(input("enter source"))
dest=int(input("enter destination"))

if src == dest:
  print("source and destination can't be same")

if src==1 and dest==2:
  fare=100
  journeyDetails='youre travelling from virar to bhayandar.'
elif src==1 and dest==3:
  fare=200
  journeyDetails = 'youre travelling from virar to borivali.'
elif src==2 and (dest==1 or dest == 3):
  fare=100
  journeyDetails = 'youre travelling from bhayandar.'
elif src==3 and dest == 1:
  fare=200
  journeyDetails = 'youre travelling from borivali to virar.'
elif src==3 and dest == 2:
  fare=100
  journeyDetails = 'youre travelling from borivali to bhayandar.'
else:
  print("you didn't select right option")

#print(src)
#print(dest)
print(journeyDetails)
print("your fare is: ",fare)

print("enter your pin to make transaction")
userpin=int(input("enter you pin"))
if userpin != pin:
  print("incorrect pin")
else:
  balance = balance - fare
  print('transaction is successful, remaining balance is ',balance)
  mycursor.execute("update customers set bal={} where username = 'krrish' ".format(balance))
  mydb.commit()