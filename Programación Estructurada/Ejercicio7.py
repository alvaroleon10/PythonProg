'''
Created on 10 oct 2022

@author: leonr
'''
num1 = int(input("How many numbers do you want input?: "))

while num1 <= 0:
    num1 = int(input("How many numbers do you want input?: "))
    
total = 0
    
for x in range (num1):
    num2 = int(input("Enter one number greater than 0: "))
    while num2 <= 0:
        num2 = int(input("The number is not valid, it should be greater than 0: "))
    total += num2
    
print(f"The medium is {total/num1}")