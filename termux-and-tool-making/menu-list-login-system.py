import os
import time
import sys

def login():
  username = input("Enter Username: ")
  password = input("Enter Password: ")

  if username != "USERNAME" and password != "PASSWORD":
    print("Wrong Username or Password")
    os.system("clear")
    login()

def main():
  os.system("clear")
  login()
  print(" Choose Your Option: ")
  print("\t1. SMS Bombing")
  print("\t2. DDos Attack")
  print("\t3. IP Tracker")
  print("\t4. Email Bombing")
  print("\t5. Short URL")
  print("\t99. About")
  print("\t00. Exit")
  
  userInput = input("\n Choice >> ")
    
  if userInput == "01" or userInput == "1":
    SMS_Bombing() #This is Demo Function Call
  elif userInput == "02" or userInput == "2":
    DDos_Attack() #This is Demo Function Call
  elif userInput == "03" or userInput == "3":
    IP_Tracer() #This is Demo Function Call
  elif userInput == "04" or userInput == "4":
    Email_Bombing() #This is Demo Function Call
  elif userInput == "05" or userInput == "5":
    Short_URL() #This is Demo Function Call
  elif userInput == "00" or userInput == "0":
    sys.exit()
  else:
    print("Wrong Input")
    sys.exit()

if __name__ == "__main__" :
  main()
