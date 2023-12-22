#!/usr/bin/env python
# coding: utf-8

# Write a python program to print “Hello Students”.

# In[1]:


print("Hello Students")


# Write a program to print your address i) using single print ii) using multiple print.

# In[6]:


print("kailash nagar, gokulnagar \njamnagar \n361004\n")
print("kailash nagar, gokulnagar")
print("jamnagar")
print('361004')


# Write a program to print addition of two numbers (without input function).

# In[7]:


print(5 + 6)


# Write a program to calculate and print average of two numbers (without input function).

# In[8]:


print((5 + 6)/2)


# Write a program to raise indentation error and correct it.

# In[11]:


if 1 == 1:
    print('yes')


# Write a program that prints "Hello-World" using seprator

# In[19]:


print('Hello','World', sep="-")


# Write a program that prints "Hello-DU Hello DU " using seperator and using end

# In[21]:


print('Hello', 'DU', sep="-", end=" ")
print("Hello","DU")


# WAP to calculate simple interest.

# In[25]:


p = float(input("Enter principle amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time in years: "))

simpleInterest = (p * r * t) / 100

print("Simple Interest:",simpleInterest)


# WAP to calculate area of triangle.

# In[27]:


height = float(input("Enter height:"))
base = float(input("Enter base:"))

areaOfTriangle = base * height * 0.5

print("Area:",areaOfTriangle)


# WAP to calculate area and circumference of circle.

# In[29]:


radius = float(input("Enter radius:"))

area = 3.14 * radius * radius
circumference = 2 * 3.14 * radius

print("Area:",area,"\nCircumference:",circumference)


# WAP to convert degree to Fahrenheit and vice versa

# In[32]:


fahrenheit = float(input("Enter temperature in Fahrenheit:"))
convertedCelsius = ((fahrenheit - 32) * 5) / 9

print(fahrenheit,"Fahrenheit is equal to",convertedCelsius,"degrees celsius.")

celsius = float(input("Enter temperature in celsius:"))
convertedFahrenheit = (celsius * (9/5)) + 32

print(celsius,"degree celsius is equal to",convertedFahrenheit,"degrees Fahrenheit.")


# WAP to calculate total marks and percentage of 5 subject

# In[35]:


s1 = float(input("Enter marks for subject 1:"))
s2 = float(input("Enter marks for subject 2:"))
s3 = float(input("Enter marks for subject 3:"))
s4 = float(input("Enter marks for subject 4:"))
s5 = float(input("Enter marks for subject 5:"))

totalMarks = s1 + s2 + s3 + s4 + s5
percentage = totalMarks / 5

print("Total:",totalMarks,"\nPercentage:",percentage,"%")


# WAP to print multiplication table without using loops.

# In[48]:


num = int(input("Enter number: "))
i = 1

print(num,"x",i,"=",(num * i))
i += 1
print(num,"x",i,"=",(num * i))
i += 1
print(num,"x",i,"=",(num * i))
i += 1
print(num,"x",i,"=",(num * i))
i += 1
print(num,"x",i,"=",(num * i))
i += 1
print(num,"x",i,"=",(num * i))
i += 1
print(num,"x",i,"=",(num * i))
i += 1
print(num,"x",i,"=",(num * i))
i += 1
print(num,"x",i,"=",(num * i))
i += 1
print(num,"x",i,"=",(num * i))
i += 1


# WAP to convert seconds into hours, minutes & seconds and print them in HH:MM:SS(with modulo and without modulo)

# In[52]:


number = int(input("Enter number of seconds: "))

h = number // 3600
s = number % 3600
m = s // 60
s %= 60

print(h,m,s,sep=":")


# In[60]:


number = int(input("Enter number of seconds: "))

h = number // 3600
s = number - (h * 3600)
m = s // 60
s = s - (m * 60)

print(h,m,s,sep=":")


# WAP to convert Days into Years, Weeks & Days with and without modulo

# In[62]:


number = int(input("Enter number of days: "))

y = number // 365
d = number % 365
w = d // 7
d %= 7

print(y,"years",w,"weeks",d,"days")


# In[63]:


number = int(input("Enter number of days: "))

y = number // 365
d = number - (y * 365)
w = d // 7
d = d - (w * 7)

print(y,"years",w,"weeks",d,"days")


# In[ ]:




