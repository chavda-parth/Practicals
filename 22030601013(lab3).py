#!/usr/bin/env python
# coding: utf-8

# ## WAP to check whether the given number is positive or negative.

# In[3]:


num = int(input("enter the number:"))

if(num < 0):
    print('Negative')
elif(num > 0):
    print('Positive')
else:
    print('Zero')


# ## WAP to check whether the given number is odd or even.

# In[11]:


num = int(input("Enter the number:"))

if(num % 2 == 0 and num != 0):
    print("Even")
elif(num % 2 != 0 and num != 0):
    print("Odd")
else:
    print("Zero")


# ## WAP to find out largest number from given two numbers.

# In[14]:


a = int(input('Enter first number (A): '))
b = int(input('Enter second number (B): '))

if(a > b):
    print('A is grater than B.')
elif(b > a):
    print('B is greater than A.')
else:
    print('Both A and B are equal.')


# ## WAP to perform Addition, Subtraction, Multiplication and Division of numbers as per user’s choice.

# In[21]:


a = float(input('Enter first number: '))
b = float(input('Enter second number: '))
choice = input('Enter operation (+, -, *, /): ')

if(choice == '+'):
    print(a, choice, b, '=', a + b)
elif(choice == '-'):
    print(a, choice, b, '=', a - b)
elif(choice == '*'):
    print(a, choice, b, '=', a * b)
elif(choice == '/'):
    print(a, choice, b, '=', a / b)
else:
    print('Invalid choice.')


# # WAP to find out largest number from given three numbers.

# In[27]:


a = int(input('Enter first number (A): '))
b = int(input('Enter second number (B): '))
c = int(input('Enter third number (C): '))

if(a >= b and a >= c):
    print('A is the largest number.')
elif(b >= a and b >= c):
    print('B is the largest number.')
elif(c >= a and c >= b):
    print('C is the largest number.')
else:
    print('All numbers are equal.')


# ## WAP to given year is leap year or not.

# In[30]:


year = int(input('Enter year: '))

if((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
    print('Leap year.')
else:
    print('Not a leap year.')


# ## WAP to check whether a number is divisible by 5 and 11 or not.

# In[34]:


num = int(input('Enter number: '))

if(num % 5 == 0 and num % 11 == 0):
    print('Yes')
else:
    print('No')


# ## WAP to input week number and print weekday.

# In[35]:


day = int(input('Enter a number(1 to 7 only): '))
if (day == 1):
    print('Monday')
elif (day == 2):
    print('Tuesday')
elif (day == 3):
    print('Wednesday')
elif (day == 4):
    print('Thursday')
elif (day == 5):
    print('Friday')
elif (day == 6):
    print('Saturday')
elif (day == 7):
    print('Sunday')
else:
    print('Invalid input')


# ## WAP to check whether entered character is vowel or not?

# In[38]:


charct = input('Enter character: ')

if(charct == 'a' or charct == 'e' or charct == 'i' or charct == 'o' or charct == 'u'):
    print('Vowel')
else:
    print('Not a vowel')


# ## WAP to input electricity unit charges and calculate total electricity bill according to the given condition:
# <pre>
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill.
# </pre>
# 

# In[40]:


unit = float(input('Enter Unit: '))
result = 0

if (unit <= 50):
    result = unit * 0.50
elif (unit <= 150):
    result = ((unit - 50) * 0.75) + 25
elif (unit <= 250):
    result = ((unit - 150) * 1.20) + 100
else:
    result = ((unit - 250) * 1.50) + 220
    
result = result + (0.2 * result)

print('Electricity Charges: ', result)


# ## WAP to read marks of five subjects. Calculate percentage and print class accordingly.    Fail below 35, Pass Class between 35 to 45, Second Class between 45 to 60, First Class between 60 to 70, Distinction if more than 70.

# In[45]:


sub1 = float(input('Enter marks for subject 1: '))
sub2 = float(input('Enter marks for subject 2: '))
sub3 = float(input('Enter marks for subject 3: '))
sub4 = float(input('Enter marks for subject 4: '))
sub5 = float(input('Enter marks for subject 5: '))

percent = (sub1 + sub2 + sub3 + sub4 + sub5)//5

if (percent < 35):
    print('Fail')
elif (percent <= 45):
    print(percent, '% Pass Class')
elif (percent <= 60):
    print(percent, '% Second Class')
elif (percent <= 70):
    print(percent, '% First Class')
else:
    print(percent, '% Distinction')


# In[ ]:




