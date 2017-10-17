import pickle

def take_backup(filename):
    ''' Take bak of file to filename.bak '''
    os.rename(filename,"%s.bak"%filename)

def load_file(filename):
    ''' Load file to a list '''
    file_content = []
    with open ('%s'%filename, 'rb') as fp:
        file_content = pickle.load(fp)
    return file_content

def dump_file(filename,list_to_dump):
    ''' Dump list to filename '''
    with open('%s'%filename, 'wb') as fp:
        pickle.dump(list_to_dump, fp)
    
def update_article_database_and_backup(old_articles,articles_to_display,filename):
    ''' Update articles to filebased database for further use'''
    new_articles = []
    new_articles = list(set(old_articles + articles_to_display))
    if len(new_articles) > 200:
        take_backup(filename)
        dump_file(filename,articles_to_display)
    else:
        dump_file(filename,new_articles)       
