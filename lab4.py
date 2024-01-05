#!/usr/bin/env python
# coding: utf-8

# ___
# <a href='https://www.darshan.ac.in/'><center> <img width=20% height=20% src='https://www.darshan.ac.in/Content/media/DU_Logo.svg'/></center></a>
# <pre>
# <center><b>Python</b></center>
# <center><b>Lab - 4(String)</b></center>    
# </pre>
# ____

# ## 01) WAP to check given string is palindrome or not.
# 

# In[10]:


a = input("Enter string")

a = a.lower()

if(a == a[::-1]):
    print("Palindrome")
else:
    print("Not palindrome")


# ## 02) WAP to reverse the word in given string.
# 

# In[83]:


string = "We Study In Darshan University"

i = 0
counter = 0

string = string[::-1]
string2 = ""

while i < len(string):
    temp = ""
    
    while(i < len(string) and str.isalpha(string[i])):
        temp = temp + string[i]
        i += 1
        
    string2 = string2 + temp[::-1] + " "
    i = i + 1
    
print(string2)


# ## 03) WAP to remove ith character from given string.

# In[99]:


string = "Hello World"
i = int(input("Enter: "))

print(string[0:i:1]+string[i + 1::])


# ## 04) WAP to print even length word in string

# In[ ]:





# ## 05) WAP to find length of String without using len function.

# In[ ]:





# ## 06) WAP to count numbers of vowels in given string.

# In[ ]:





# ## 07) WAP to do String slicing
# 
#  a)	Left (Or anticlockwise) rotate the given string by d elements (where d <= n).
#  
#  
#  b)	Right (Or clockwise) rotate the given string by d elements (where d <= n).
# 
#  

# In[ ]:





# ## 08) WAP to count of o in this string. “RCqIoMkolU”   

# In[ ]:





# <pre>
# <h3><p style="color:red">EXTRA</p> </h3>
# </pre>

# ## 01) WAP which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".

# In[ ]:





# ## 02) WAP to find all duplicate characters in string.

# In[ ]:




