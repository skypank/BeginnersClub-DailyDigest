import pickle
import masterlist

display_articles = []
   
for filename in masterlist.lofiles:
    articles_to_display = []
    with open ('%s'%filename, 'rb') as fp:
        articles_to_display = pickle.load(fp)
    if len(articles_to_display) > 0:
        for link in articles_to_display:
            display_articles.append(link)     

with open ('testlist', 'wb') as mrp:
    pickle.dump(display_articles,mrp)
