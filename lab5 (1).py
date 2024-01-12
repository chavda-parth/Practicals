#!/usr/bin/env python
# coding: utf-8

# ___
# <a href='https://www.darshan.ac.in/'><center> <img width=20% height=20% src='https://www.darshan.ac.in/Content/media/DU_Logo.svg'/></center></a>
# <pre>
# <center><b>Python</b></center>
# <center><b>Lab - 5(LOOP)</b></center>    
# </pre>
# ____

# <pre>
# <h3> <p style="color:red"> USING WHILE LOOP</p> </h3>
# </pre>

# ## 1) WAP to print 1 to n

# In[1]:


n = int(input('Enter n: '))

i = 1

while (i <= n):
    print(i)
    i += 1


# ## 2)WAP to print odd numbers between given two numbers.

# In[4]:


a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

i = a

while (i <= b):
    if(i % 2 != 0):
        print(i)
    i += 1


#  ## 3) WAP to print n number of sum

# In[5]:


n = int(input('Enter n: '))

i = 1
addition = 0

while (i <= n):
    addition += i
    i += 1

print(addition)


# ## 4) WAP to print sum of digits of given number.

# In[7]:


num = int(input('Enter number: '))

temp = num
dsum = 0

while (temp > 0):
    mod = temp % 10
    temp = temp // 10
    dsum += mod
    
print(dsum)


# ## 5)  WAP to find whether the given number is prime or not.

# In[11]:


n = int(input('Enter number: '))

i = 2
flag = 0

while (i < n):
    if (n % i == 0):
        flag = 1
        break
    
    i += 1
    
if (flag == 0):
    print('Prime')
else:
    print('Not Prime')


# <pre>
# <h3><p style="color:red"> USING FOR LOOP </p> </h3>
# </pre>

# ## 7) WAP to print sum of series 1–2+3–4+5–6+7...n

# In[15]:


n = int(input('Enter n: '))

i = 1
result = 0

for i in range(n + 1):
    if (i % 2 != 0):
        result += i
    else:
        result -= i
        
print(result)


# ## 8) WAP to print multiplication table of given number.(using for loop)

# In[18]:


num = int(input('Enter number: '))

for i in range(11):
    print(num, ' x ', i, ' = ', (num * i))


# ## 9) WAP to find factorial of the given number.

# In[22]:


num = int(input('Enter number: '))

fact = 1

for i in range(num):
    fact += fact * i
    
print(fact)


# ## 10) WAP to find out prime numbers between given two numbers.

# In[25]:


a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
flag += 0


# <h3><p style="color:red">EXTRA</p></h3>

# ## 1) WAP to Find largest prime factor of given number.
# 

# In[ ]:





# ## 2) WAP to print Fibonacci series up to number given by user.

# In[ ]:





# 
# ## 3) WAP to print all the number which are divisible by 11 but not divisible by 2 betweengiven two numbers.

# In[ ]:




