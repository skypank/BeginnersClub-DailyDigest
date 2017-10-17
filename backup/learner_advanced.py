import pickle
from urllib.parse import urlparse 
import difflib
import time
import utils
import re

def parse_url(link):
    '''Parse url to get only article headline'''
    obj = urlparse(link)
    path = obj.path
    name = path.split('/')
    element = name[-1:]
    if element == ['']:
        element = name[-3].split()
    return element

def get_similarity_ratio(a,b):
    '''Compare two string and return similarity ratio'''
    return difflib.SequenceMatcher(None,a,b).ratio()

def rank_on_score(words, new_list):
    '''Rank article based on headline'''
    score = 0
    for link in new_list:
        new_score = get_similarity_ratio(str(link),str(words))
        if new_score > score:
            score = new_score
    #print(words,score)
    return score 

def publish_grade(link_words,grade):
    
    if grade:
        heading = re.sub('[-]', ' ', str(link_words))
        #print(heading.split())
        #regex_var = re.compile('(invest|strong|industry|sugar)')
        if re.search('(strategy|investing|good|shock|portfolio|' \
                       'smart|top|great|return|destroy|crash|bottom|' \
                       'wealth|poor|war|energy)',str(heading)):
            return True
        return False
    return True
        
#new_list = []
def remove_similar_by_matching_headline(list_of_link,matching_ratio,grade):
    new_list = []
    match_list = []
    #print("Before : %s"%len(list_of_link))
    #remove similar
    #print(grade)
    for i,link in enumerate(list_of_link):
        #print("Before parse : %s"%link)
        link_words = parse_url(link)
        #print("After parse : %s" %link_words)
        
        if link_words not in new_list and \
           publish_grade(link_words,grade) and \
           rank_on_score(link_words,new_list) < matching_ratio:
            
            new_list.append(link_words)
            match_list.append(link)
            
    return match_list

'''
#Initialize articles to read            
display_articles = []
display_articles= utils.load_file('master-backup26082017.readerslist')

#Initial count
print("Before : %s"%len(display_articles))
#print("\n".join(display_articles))
#Filter based on article headline similarity
start= time.time()
matching_ratio = 0.5
grade = True
display_articles = remove_similar_by_matching_headline(display_articles,matching_ratio,grade)
end = time.time()
#Final count
print("After : %s"%len(display_articles))
print ("\nTook {} seconds".format(end - start))
#print("\n".join(display_articles))
#print(new_list)
'''
