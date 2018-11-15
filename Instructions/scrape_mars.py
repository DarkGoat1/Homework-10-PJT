
# coding: utf-8

# In[1]:

def scrape():

    from bs4 import BeautifulSoup
    from splinter import Browser
    import requests
    import lxml
    import time


    # In[2]:
    masterdict = {}

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)


    # In[3]:


    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)


    # In[4]:


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    # In[5]:


    response = requests.get(url)


    # In[ ]:





    # In[6]:




    title1 = soup.find_all('div', class_="content_title")

    titles=[]

    title1
    for x in title1:
        titles.append(x.find('a').text.replace("\n", ""))

    titles

    masterdict['titles'] = titles


    # In[7]:


    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url2)
    html2 = browser.html
    soup2 = BeautifulSoup(html2, 'html.parser')


    # In[8]:


    featuredimg = soup2.find_all('article', class_="carousel_item")
    imgurl = [tag['style'] for tag in soup2.findAll('article')]


    imgurl1 = imgurl[0].replace("background-image: url('", "")
    imgurl2 = imgurl1.replace("');", "")

    finalimgurl = f'https://www.jpl.nasa.gov' + f'{imgurl2}'

    finalimgurl

    masterdict['imageURL'] = finalimgurl

    # In[9]:


    url3 = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url3)
    html3 = browser.html
    soup3 = BeautifulSoup(html3, 'html.parser')

    memes = soup3.find_all('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")

    mars_temp = memes[0].text

    mars_temp

    masterdict['MarsTemperature'] = mars_temp

    # In[24]:


    url4 = 'https://space-facts.com/mars/'
    browser.visit(url4)
    html4 = browser.html
    soup4 = BeautifulSoup(html4, 'html.parser')

    table = soup4.find_all('table', class_="tablepress tablepress-id-mars")

    label = []
    param = []

    for x in table:
        meme2 = x.find_all('strong')
    for y in meme2:
        label.append(y.text)
        
    for z in table:
        meme3 = z.find_all('td', class_="column-2")
    for a in meme3:
        param.append(a.text)

    tempmemes = tuple(zip(label, param))
    tempmemes

    masterdict['MarsInfo'] = tempmemes
    return masterdict
