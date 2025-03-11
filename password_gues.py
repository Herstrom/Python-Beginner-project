
import random
#import randome for gues randomely number
#Asking name to the user for nake a strong password with their name.
name=input("Enter your name:")
number="0123456789"
symbol="!@#$%^&*()_-./,"

combine=number+symbol
length=int(input("Enter your length of the password:"))
password="".join(random.sample(combine,length))
print(name+password)