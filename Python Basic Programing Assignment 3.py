#!/usr/bin/env python
# coding: utf-8
	•	Write a Python Program to Check if a Number is Positive, Negative or Zero?
	•	Write a Python Program to Check if a Number is Odd or Even?
	•	Write a Python Program to Check Leap Year?
	•	Write a Python Program to Check Prime Number?
	•	Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?

# In[4]:


# Write a Python Program to Check if a Number is Positive, Negative or Zero?
a = int(input("Enter a number you want to check positive Negative or Zero:"))
if a >0:
    print("Number is greater then Zero",a)
elif a == 0:
    print("Number is equal to zero",a)
else:
    print("Number is negative",a)


# In[10]:


## 	Write a Python Program to Check if a Number is Odd or Even?
a = int(input("Enter a number you want to check  if a Number is Odd or Even:"))
if a%2==0:
    print("Number is even ",a)
else :
    print("Number is odd")
    


# In[13]:


# • Write a Python Program to Check Leap Year?
year = int(input("Enter a year you want to Check Leap Year:"))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))


# In[28]:


## Write a Python Program to Check Prime Number?
a = int(input("Enter a number you want to check  if a Number is prime or not:"))
if a >1:
    for i in range(2,a):
        if (a%i)==0:
            
            print("Number is not prime:",a)
            break
    else: 
        print("Number is  prime:",a)
else:
    print(a,"is not a prime number")


# In[29]:


### Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
lower = 2
upper = 10001

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(2, 10001):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)


# In[ ]:




