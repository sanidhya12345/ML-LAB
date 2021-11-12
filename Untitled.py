#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt

x_values=[0,1,2,3,4,5]
squares=[0,1,4,9,16,25]

plt.plot(x_values,squares)
plt.savefig("testimage.jpg")


# In[2]:


x=[5,2,7]
y=[2,16,4]
plt.plot(x,y)
plt.title('info')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()


# In[3]:


x=[1,2,3,4,5]
y=[50,40,70,80,20]
y2=[80,20,20,50,60]
y3=[70,20,60,40,60]
y4=[80,20,20,50,60]

plt.plot(x,y,'g',label='enfield',linewidth=5)
plt.plot(x,y2,'c',label='honda',linewidth=5)
plt.plot(x,y3,'k',label='yamaha',linewidth=5)
plt.plot(x,y4,'y',label='ktm',linewidth=5)
plt.title('bike details in line plot')
plt.ylabel("distance in kms")
plt.xlabel('days')
plt.legend()


# In[5]:


x_values=[5,6,3,7,2]
y_values=["A","B","C","D","E"]
plt.bar(y_values,x_values,color="pink")
plt.show()


# In[8]:


plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],label="enfield",width=0.5)
plt.bar([0.26,1.25,2.25,3.25,4.25],[50,40,70,80,20],label="honda",color='r',width=0.5)
plt.bar([0.31,1.5,2.5,3.5,4.5],[50,40,70,80,20],label="yamaha",color='y',width=0.5)
plt.bar([0.75,1.75,2.75,3.75,4.75],[50,40,70,80,20],label="ktm",color='g',width=0.5)

plt.legend()
plt.xlabel('days')
plt.ylabel('distance in kms')
plt.title('bike details in bar plotting')


# In[9]:


x_values=[5,6,3,7,2]
y_val=["A","B","C","D","E"]
plt.barh(y_val,x_values,color="yellowgreen")
plt.show()


# In[15]:


import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Users\GLAU\Downloads\nba.csv')
print(df)


# In[17]:


y_values = df['Salary']
x_values = df['Age']
plt.xlabel('Age')
plt.ylabel('Salary (in millions)')
#To plot a bar graph plt.bar() command is used
#This plots a bar graph between Age and Salaries of NBA players
plt.bar(x_values,y_values,color = "purple")
plt.show()


# In[18]:


y_values = df['Salary']
x_values = df['Age']
plt.xlabel('Age')
plt.ylabel('Salary (in millions)')
# Making changes in the color field changes the colour of the graph
plt.bar(x_values,y_values,color = "khaki")
plt.show()


# In[ ]:




