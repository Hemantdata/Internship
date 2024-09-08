#!/usr/bin/env python
# coding: utf-8

# In[2]:


import bs4 
import requests
url= "https://www.cnbc.com/world/?region=world"
res= requests.get(url)
print("object",type(res))
soup = bs4.BeautifulSoup(res.text,'html.parser')
print("object",type(soup))


# In[6]:


scraped_headings = soup.find_all('div', class_='RiverHeadline')
scraped_headings


# In[ ]:


<div class="-headline RiverHeadline-hasThumbnail"><a href="https://www.cnbc.com/2024/09/06/ai-craze-getting-funded-by-tech-giants-distorting-traditional-vcs.html">AI craze is distorting VC market, as tech giants Microsoft and Amazon pour in billions of dollars</a></div>


# In[ ]:




