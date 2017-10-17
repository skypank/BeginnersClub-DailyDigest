display_articles = ['1','2','3','4']

print("Lenght before delete %s"%len(display_articles))
count=int(input())
for i,link in enumerate(display_articles):
    if i < count:
        print("item : "+link)#del display_articles[i]
del display_articles[:count]

print("Lenght after delete %s"%len(display_articles))
print(display_articles)
