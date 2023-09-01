from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import numpy as np 

options = webdriver.EdgeOptions()
options.add_experimental_option('detach',True)
driver = webdriver.Edge(options=options)
url = 'https://www.adducation.info/general-knowledge-travel-and-transport/emergency-numbers/'


driver.get(url)
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(10)

containers = driver.find_elements(by='xpath', value='//tr')

Country = []
Emergency = []
Police = []
Ambulance = []
Fire = []
Group = []
Calling_codes = []
Local_emergency_no = []


P=range(1,240)
for i,j in zip(containers,P):
    try:
        A = i.find_element(by='xpath',value=f'//tr[{j}]/td[1]/strong').text  
        B = i.find_element(by='xpath',value=f'//tr[{j}]/td[2]').text
        C = i.find_element(by='xpath',value=f'//tr[{j}]/td[3]').text
        D = i.find_element(by='xpath',value=f'//tr[{j}]/td[4]').text
        E = i.find_element(by='xpath',value=f'//tr[{j}]/td[5]').text
        F = i.find_element(by='xpath',value=f'//tr[{j}]/td[6]').text
        G = i.find_element(by='xpath',value=f'//tr[{j}]/td[7]').text
        H = i.find_element(by='xpath',value=f'//tr[{j}]/td[8]').text
    
    except:
        A = i.find_element(by='xpath',value=f'//tr[{j}]/td[1]/em/strong').text
        B = i.find_element(by='xpath',value=f'//tr[{j}]/td[2]').text
        C = i.find_element(by='xpath',value=f'//tr[{j}]/td[3]').text
        D = i.find_element(by='xpath',value=f'//tr[{j}]/td[4]').text
        E = i.find_element(by='xpath',value=f'//tr[{j}]/td[5]').text
        F = i.find_element(by='xpath',value=f'//tr[{j}]/td[6]').text
        G = i.find_element(by='xpath',value=f'//tr[{j}]/td[7]').text
        H = i.find_element(by='xpath',value=f'//tr[{j}]/td[8]').text
    

    finally:
        Country.append(A)
        Emergency.append(B)
        Police.append(C)
        Ambulance.append(D)
        Fire.append(E)
        Group.append(F)
        Calling_codes.append(G)
        Local_emergency_no.append(H)

driver.quit()

dict_={'Country' : Country,
    'Emergency' : Emergency, 
    'Police' : Police, 
    'Ambulance' : Ambulance, 
    'Fire' : Fire, 
    'Continent' : Group, 
    'Calling_codes' : Calling_codes,
    'Local_emergency_no' : Local_emergency_no
    }


#Data Wrangling 
Emergency_DS = pd.DataFrame(dict_)
Emergency_DS.replace('','-',inplace = True)

Emergency_DS['alpha-2 code']=np.nan
Emergency_DS['Countries']=np.nan
Emergency_DS['Continental Region']=np.nan

Emergency_DS['alpha-2 code']=Emergency_DS['Country'].str[0:2]
Emergency_DS['Countries']=Emergency_DS['Country'].str[3:]
Emergency_DS['Continental Region']=Emergency_DS['Continent']
Emergency_DS.drop(['Country'],axis=1)

Emergency_DS=Emergency_DS[['alpha-2 code','Countries', 'Emergency', 'Police', 'Ambulance',
       'Fire', 'Continental Region', 'Calling_codes', 'Local_emergency_no',]]

Emergency_DS.to_csv('Emergency_Scraper.csv')

