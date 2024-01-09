import random as r
def otpgen():
    otp=""
    for i in range(4):
        otp+=str(r.randint(1,9))
    print(f'Please do not share this one time password with anyone except vaibhav😎. Your One Time Password is {otp}')
otpgen()
'''
import random as r
# function for otp generation
def otpgen():
    otp=""
    for i in range(4):
        otp+=str(r.randint(1,9))
    print (f"Your One Time Password is "otp"")
    print ()
otpgen()

# import modules 
import math as m
import random as r
  
# function to generate OTP 
def OTPgen() : 
  
    # Declare a string variable   
    # which stores all alpha-numeric characters 
    string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    OTP = "" 
    varlen= len(string) 
    for i in range(6) : 
        OTP += string[m.floor(r.random() * varlen)] 
  
    return (OTP) 
  
# main function 
if __name__ == "__main__" : 
      
    print("Your One Time Password is ", OTPgen())
'''
aashiq hu mai dil ka mujhe jeena mat sikha
