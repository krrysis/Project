from connector import *
from variables import *


#we fetch the balance of the current user into a variable
mycursor.execute("select bal from customers where username = '{}' ".format(user))

def static():
  myresult = mycursor.fetchall()
  temp = str(myresult[0])
  return temp

balance=int(static()[1:-2])
#print(balance)

#we fetch the pin
mycursor.execute("select pin from customers where username = 'krrish' ")

pin=int(static()[1:-2])
#print(pin)
