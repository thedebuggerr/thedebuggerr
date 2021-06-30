""" Brute firce password cracker
""" 
import pyttsx3 as p 
engine=p.init()
engine.say("hello and welcome to our Bruteforce password cracker")
engine.runAndWait()
import random
import pyautogui

chars="abcdefghijklmnopqrstuvwxyz0123456789"
chars_list=list(chars)

password=pyautogui.password("enter a password: \n")
guess_password=" "
while(guess_password != password):
    guess_password = random.choices(chars_list,k=len(password))

    print("<====================" + str(guess_password) + "====================>")
    if (guess_password == list(password)):
        print("your password is :" + "", guess_password)
        break
print("\n \nthank you for using our brute force software created by _the.debugger_")
engine.say("thank you for using our brute force software created by the debugger")
engine.runAndWait()


"""                                          _the.debugger_














"""

