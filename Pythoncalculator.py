import pandas as pd
import numpy as np


def sum():
    num1=float(input("Enter the num: "))
    num2= float(input("Enter the num: "))
    sum=num1+num2
    print("Sum of 2 numbers are: ",sum )
    return sum 



def sub():
    num1=float(input("Enter the num1: "))
    num2=float(input("Enter the num2: "))
    subtraction=num1-num2
    print("Subtraction of two numbers are: ",subtraction)
    return subtraction


def mul():
    num1=float(input("Enter the number 1: "))
    num2=float(input("Enter the num2: "))
    mult=num1*num2
    print("Multiplication of two numbers",mult)
    return mult


def div():
    num1=float(input("Enter the num1: "))
    num2=float(input("Enter the number2: "))
    if num2!=0:
     return num1/num2
    else:
      print("Cannot multiply by zero")
    



while True:
   print("Select operations")
   print("1: Addition")
   print("2: Subtraction")
   print("3: Multiplication")
   print("4: Division")

   choice=input("Enter the choice from (1-4): ")
   if choice  in ('1','2','3','4'):
      if choice=='1':
         result=sum()
      elif choice=='2':
         result= sub()
      elif choice=='3':
        result= mul()
      elif choice=='4':
        result=div()

        if result is not None:
           print("Result", result)
   else:
    print("Invalid choice please enter the number from (1-4)")
      