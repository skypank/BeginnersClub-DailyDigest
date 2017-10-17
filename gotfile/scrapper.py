from bs4 import BeautifulSoup
import requests
import re
import pickle
import os
import utils

def read_articles_from_url(url,regex_var,old_articles):
    ''' Get links from url based on regex pattern '''
    r  = requests.get("http://" +url)
    data = r.text
    soup = BeautifulSoup(data,"html.parser")
    articles_to_display = []
    for link in soup.find_all('a'):        
        #Applying rules as stored in .cfg file
        if re.match(regex_var, str(link.get('href')))and (link.get('href') not in articles_to_display) and (link.get('href') not in old_articles):
            if re.match('(^(http|www)(.*))', str(link.get('href'))):
                articles_to_display.append(link.get('href'))
    return articles_to_display
    
def scrap_url_with_rules_and_data(filename):
    ''' Read config, read old articles and get links
    from url and return list of articles to '''

    #read config files for url and regex rules
    configs = utils.load_file("%s.cfg"%filename)
    url = configs[0]
    regex_var = configs[1]
    
    #open filename to read old articles link
    old_articles = utils.load_file(filename)
  
    #reading links from url
    articles_to_display = list(set(read_articles_from_url(url,regex_var,old_articles)))
    
    if len(articles_to_display) > 0 :
        utils.update_article_database_and_backup(old_articles,articles_to_display,filename)
                
    return articles_to_display
