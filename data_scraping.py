#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv
import os
from time import sleep
from bs4 import BeautifulSoup
from requests import get
from selenium import webdriver
from selenium.webdriver.support.ui import Select

DRIVER_PATH = 'C:/Users/Akashah/Downloads/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://www.fashiondatabase.com/database#')

select = Select(driver.find_element_by_id('edit-field-bd-main-category-tid-selective'))
select.select_by_visible_text('Fashion Brand')
sleep(5)
driver.find_element_by_xpath("//input[@type='submit'][@value='Apply']").click()

file_out = r'C:\Users\Akashah\Downloads\OutFile.csv'
header = ['Name']

with open(file_out, "w", newline='', encoding='utf-8') as outFile:
    writer = csv.writer(outFile)
    writer.writerow(header)
    sleep(5)
    
    for page in range(100):
        index = str(page)
        print(index)
        url = "https://www.fashiondatabase.com/database?field_bd_main_category_tid_selective=25114&field_bd_country_tid_selective=All&page="+index
        response = get(url,headers={'Referer': 'https://www.google.com/''})
        html_soup = BeautifulSoup(response.text, 'html.parser')
        containers = html_soup.find_all('div', class_ = 'views-field views-field-title')
        for container in containers:
            row = []
            print(container.find('a').text.strip('\n'))
        sleep(2)


# In[ ]:


import csv
import os
from time import sleep
from bs4 import BeautifulSoup
from requests import get

def myfunc (container):
    row = []
    row.append(container.find('div', class_ = 'views-field views-field-title').find('a').text.strip('\n'))
    country = container.find('div', class_ = 'views-field views-field-field-bd-country')
    if country != None:
        row.append(country.find('span', class_ = 'field-content').text.strip('\n'))
    else:
        row.append('')
    
    city = container.find('div', class_ = 'views-field views-field-field-bd-city')
    if city != None:
        row.append(city.find('span', class_ = 'field-content').text.strip('\n'))
    else:
        row.append('')
    address = container.find('div', class_ = 'views-field views-field-field-bd-address')
    if address != None:
        row.append(address.find('span', class_ = 'field-content').text.strip('\n'))
    else:
        row.append('')
    tel = container.find('div', class_ = 'views-field views-field-field-bd-tel')
    if tel != None:
        row.append(tel.find('span', class_ = 'field-content').text.strip('\n'))
    else:
        row.append('')
    website = container.find('div', class_ = 'views-field views-field-field-bd-website') 
    if website != None:
        row.append(website.find('span', class_ = 'field-content').text.strip('\n'))
    else:
        row.append('')
    fb = container.find('div', class_ = 'views-field views-field-field-bd-facebook')
    if fb != None:
        row.append(fb.find('span', class_ = 'field-content').text.strip('\n'))
    else:
        row.append('')
    tw = container.find('div', class_ = 'views-field views-field-field-bd-twitter')
    if tw != None:
        row.append(tw.find('span', class_ = 'field-content').text.strip('\n'))
    else:
        row.append('')
    yt = container.find('div', class_ = 'views-field views-field-field-bd-youtube')
    if yt != None:
        row.append(yt.find('span', class_ = 'field-content').text.strip('\n'))
    else:
        row.append('')
    return row

file_out = r'C:\Users\Akashah\Downloads\OutFile.csv'
header = ['Name of Brand','Country','City','Address','Contact','Website','Facebook','Twitter','Youtube']

with open(file_out, "w", newline='', encoding='utf-8') as outFile:
    writer = csv.writer(outFile)
    writer.writerow(header)
    sleep(5)
    
    for page in range(100):
        index = str(page)
        row = []
        url = "https://www.fashiondatabase.com/database?field_bd_main_category_tid_selective=25114&field_bd_country_tid_selective=All&page="+index
        response = get(url)
        html_soup = BeautifulSoup(response.text, 'html.parser')
        row = myfunc(html_soup.find('div', class_ = 'views-row views-row-1 views-row-odd views-row-first')) 
        writer.writerow(row)    
        row = myfunc(html_soup.find('div', class_ = 'views-row views-row-2 views-row-even')) 
        writer.writerow(row)  
        row = myfunc(html_soup.find('div', class_ = 'views-row views-row-3 views-row-odd')) 
        writer.writerow(row)  
        row = myfunc(html_soup.find('div', class_ = 'views-row views-row-4 views-row-even')) 
        writer.writerow(row)  
        row = myfunc(html_soup.find('div', class_ = 'views-row views-row-5 views-row-odd')) 
        writer.writerow(row)  
        row = myfunc(html_soup.find('div', class_ = 'views-row views-row-6 views-row-even views-row-last')) 
        writer.writerow(row)    
        sleep(1)


# In[ ]:


import csv
import os
from time import sleep
from bs4 import BeautifulSoup
from requests import get
from selenium import webdriver
from selenium.webdriver.support.ui import Select

DRIVER_PATH = 'C:/Users/Akashah/Downloads/chromedriver'
download_dir = 'C:/Temp_Doc'
pdf_ext = "?spoilerPDF=on&Dernires-mises--jour=on&Sources=on&Sommaire=on&notesPDF=on&dlPDF=submitted"
url = "https://www.medg.fr/fiches-maladie-et-grand-syndrome/"
response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
titles = html_soup.find('ul', class_ = 'lcp_catlist').find_all('a')
count = 0
chunk_size = 2000
for title in titles:
    fileName = 'C:/Users/Akashah/Downloads/pdfs/'+title.get('href')[20:-1]+'.pdf'
    file_url = title.get('href') + "?spoilerPDF=on&Dernires-mises--jour=on&Sources=on&Sommaire=on&notesPDF=on&dlPDF=submitted.pdf"
    with open(fileName, "wb") as file:
        print(file_url)
        r = get(file_url, stream=True, headers={'Referer': 'https://www.google.com/'})
        for chunk in r.iter_content(chunk_size):
            file.write(chunk)
    count = count + 1
    print(title.get('href'))
    if count == 50 :
        break
    sleep(randrange(10))
print(count)


# In[ ]:


st = 'jsfgislurihwksncsufw'
print(st[5:])


# In[23]:


import csv
import os
import random
from time import sleep
from bs4 import BeautifulSoup
from requests import get
from selenium import webdriver
from selenium.webdriver.support.ui import Select

table =[]
table_out = []
header = []
with open(file_in, 'r', newline='', encoding='utf-8') as inFile:
    reader = csv.reader(inFile)
    header = next(reader)
    header.append('water frontage')
    header.append('sewer frontage')
    header.append('Year Built')
    for row in reader:
        table.append(row)
table_out = header
DRIVER_PATH = 'C:/Users/Akashah/Downloads/chromedriver'
file_in = r'C:\Users\Akashah\Downloads\Winnipeg Addresses.csv'
file_out = r'C:\Users\Akashah\Downloads\OutFile.csv'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

for row in table:
    driver.get('http://www.winnipegassessment.com/AsmtTax/English/Propertydetails/default.stm')
    sbox1 = driver.find_element_by_id('StreetNumber')
    sbox1.send_keys(row[0])
    sbox2 = driver.find_element_by_id('StreetName')
    sbox2.send_keys(row[2])
    select = driver.find_element_by_id('SubmitAddress')
    select.click()
    sleep(random.randint(0,6))
    url = driver.getCurrentUrl();
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    tables = html_soup.find_all('table', class_ = 'tblAlign')

    count = 1
    for table in tables:
        if count == 1:
            count = 2
        else if count == 2:
            count = 3
            for tr in table.find_all('td'):
                print(tr[3].text)
        else if count == 3:
            


# In[19]:


import random
a = [1,2,3]
a.append(2)

"http://www.winnipegassessment.com/AsmtPub/english/propertydetails/details.aspx?pgLang=EN&isRealtySearch=true&StreetNumber=321&StreetName=alfred"
a


# In[1]:


import csv
import os
from time import sleep
from bs4 import BeautifulSoup
from requests import get
from selenium import webdriver
from selenium.webdriver.support.ui import Select

DRIVER_PATH = 'C:/Users/Akashah/Downloads/chromedriver'
download_dir = 'C:/Temp_Doc'
pdf_ext = "?spoilerPDF=on&Dernires-mises--jour=on&Sources=on&Sommaire=on&notesPDF=on&dlPDF=submitted"
url = "https://www.vocaladvancement.com/en-us/find-a-teacher"
response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
print(html_soup)
# titles = html_soup.find('ul', class_ = 'lcp_catlist').find_all('a')
# count = 0
# chunk_size = 2000
# for title in titles:
#     fileName = 'C:/Users/Akashah/Downloads/pdfs/'+title.get('href')[20:-1]+'.pdf'
#     file_url = title.get('href') + "?spoilerPDF=on&Dernires-mises--jour=on&Sources=on&Sommaire=on&notesPDF=on&dlPDF=submitted.pdf"
#     with open(fileName, "wb") as file:
#         print(file_url)
#         r = get(file_url, stream=True, headers={'Referer': 'https://www.google.com/'})
#         for chunk in r.iter_content(chunk_size):
#             file.write(chunk)
#     count = count + 1
#     print(title.get('href'))
#     if count == 50 :
#         break
#     sleep(randrange(10))
# print(count)


# In[ ]:




