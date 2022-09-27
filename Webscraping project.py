#!/usr/bin/env python
# coding: utf-8

# In[11]:


from bs4 import BeautifulSoup as bs
import requests


# In[12]:


link="https://www.flipkart.com/hp-15s-ryzen-3-dual-core-3250u-8-gb-1-tb-hdd-256-gb-ssd-windows-10-home-15s-gr0012au-laptop/p/itm9e1f8deeed35f?pid=COMFZHFWBE7APPH2&lid=LSTCOMFZHFWBE7APPH2PLTTEQ&marketplace=FLIPKART&cmpid=content_computer_15083003945_u_8965229628_gmc_pla&tgi=sem,1,G,11214002,u,,,556262839325,,,,c,,,,,,,&gclid=Cj0KCQjw6_CYBhDjARIsABnuSzpef_B2LBXLrtVSa2-jth0eeThYb51_sW9hajIIguzyBPELj6zvERoaAr2-EALw_wcB"


# In[14]:


page=requests.get(link)


# In[15]:


page


# In[16]:


page.content


# In[18]:


soup=bs(page.content,"html.parser")


# In[19]:


soup


# In[20]:


print(soup.prettify())


# In[24]:


title=soup.title
print(title)
print(type(title))
print(title.string)


# In[26]:


price=soup.find_all("div",class_="_30jeq3 _16Jk6d")
price


# In[27]:


product_price=[]
for i in range(0,len(price)):
    product_price.append(price[i].get_text())
product_price


# In[28]:


customer=soup.find_all("p",class_="_2sc7ZR _2V5EHH")
customer


# In[29]:


cust_name=[]
for i in range(0,len(customer)):
    cust_name.append(customer[i].get_text())
cust_name


# In[30]:


comment=soup.find_all("p",class_="_2-N8zT")
comment


# In[31]:


cust_comment=[]
for i in range(0,len(comment)):
    cust_comment.append(comment[i].get_text())
cust_comment


# In[32]:


star=soup.find_all("div",class_="_3LWZlK _1BLPMq")
star


# In[33]:


cust_star=[]
for i in range(0,len(star)):
    cust_star.append(star[i].get_text())
cust_star


# In[36]:


review=soup.find_all("div",class_="t-ZTKy")
review


# In[37]:


cust_review=[]
for i in range(0,len(review)):
    cust_review.append(review[i].get_text())
cust_review


# In[38]:


import pandas as pd


# In[40]:


df=pd.DataFrame()
df["Customer_Name"]=cust_name
df["Rating"]=cust_star
df["Review"]=cust_review
df["Comment"]=cust_comment
df


# In[41]:


df.to_csv("FlipKart.csv",index=False)


# In[42]:


df1=pd.read_csv("FlipKart.csv")


# In[43]:


df1


# ![](web.png)

# In[ ]:




