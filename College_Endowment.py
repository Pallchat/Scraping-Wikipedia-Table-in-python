# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 12:26:49 2019

@author: PCHATTERJEE
"""

import requests
from bs4 import BeautifulSoup
import re
import time


start_time = time.time()

#
out_file = open('Wikipedia_CollegeEndowment.csv', 'w+', encoding = "utf-8")
out_file.write('College, STABR, 2018($bn), 2017($bn), 2016($bn), 2015($bn), 2014($bn), 2013($bn), 2012($bn), 2011($bn), 2010($bn), 2009($bn), 2008($bn), 2007($bn)' + '\n')


# Setting the user-agent header to look like a browser 
url = "https://en.wikipedia.org/wiki/List_of_colleges_and_universities_in_the_United_States_by_endowment"
agent = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
r = requests.get(url, headers=agent)
html_soup = BeautifulSoup(r.content, 'html.parser')

city_table = html_soup.find('table', {'class':"wikitable sortable"})

a_tag = city_table.find_all('tr')

i = 0
for s in a_tag:
    i += 1  
    if i > 1:
        name = s.find_next('a').get('href')
        college = s.find_next('a')
        coll = college.text.replace(',', ' - ').strip()
        print(coll)
        
        state = s.find_next('a').find_next('td')
        st = state.text.strip()
        print(st)
        
        end2018 = s.find_next('a').find_next('td').find_next('td')
        en2018 = end2018.text.replace('$','').strip()
        print(en2018)
        
        end2017 = s.find_next('a').find_next('td').find_next('td').find_next('td')
        if end2017.contents != None:
            en2017 = end2017.contents[0].replace('$', '').strip()
            print(en2017)
        else:
            en2017 = 'N/A'
            print(en2017)
        
        end2016 = end2017.find_next('td')
        en2016 = end2016.contents[0].replace('$', '').strip()
        print(en2016)
        
        end2015 = end2016.find_next('td')
        en2015 = end2015.contents[0].replace('$', '').strip()
        print(en2015)
        
        end2014 = end2015.find_next('td')
        en2014 = end2014.contents[0].replace('$', '').strip()
        print(en2014)
        
        end2013 = end2014.find_next('td')
        en2013 = end2013.contents[0].replace('$', '').strip()
        print(en2013)
        
        end2012 = end2013.find_next('td')
        en2012 = end2012.contents[0].replace('$', '').strip()
        print(en2012)
        
        end2011 = end2012.find_next('td')
        en2011 = end2011.contents[0].replace('$', '').strip()
        print(en2011)
        
        end2010 = end2011.find_next('td')
        en2010 = end2010.contents[0].replace('$', '').strip()
        print(en2010)
        
        end2009 = end2010.find_next('td')
        en2009 = end2009.contents[0].replace('$', '').strip()
        print(en2009)
        
        end2008 = end2009.find_next('td')
        en2008 = end2008.contents[0].replace('$', '').strip()
        print(en2008)
        
        end2007 = end2008.find_next('td')
        en2007 = end2007.contents[0].replace('$', '').strip()
        print(en2007)
        
        out_file.write(','.join(map(str, [coll, st, en2018, en2017, en2016, en2015, en2014, en2013, en2012, en2011, en2010, en2009, en2008, en2007])) + '\n')
        
    
out_file.close()

print("--- %s seconds ---" % (time.time() - start_time))   

