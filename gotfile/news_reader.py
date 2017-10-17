import masterlist #remove after making one readerlis at server instead of multiple
import pickle
import webbrowser
import time
import paramiko

#import learner #improve step by step
  
def connect_to_server(IP,uname,passwd):
   '''connect to photon server'''
   ssh = paramiko.SSHClient()
   ssh.set_missing_host_key_policy(
    paramiko.AutoAddPolicy())
   ssh.connect(IP, username=uname, 
    password=passwd)
   return ssh

def set_file_via_ftp(action,remotefilename,localfilename,ssh):
   '''Perform file action via ftp'''
   ftp = ssh.open_sftp()
   if action == 'get':
      ftp.get(remotefilename,localfilename)
   elif action == 'put':
      ftp.put(remotefilename,localfilename)
   ftp.close()

def get_reader_list(filename,ssh):
   '''Update reader list with latest news'''
   articles_to_display = []
   remotefilename = '/usr/src/scrapper/%s.readerslist'%filename
   localfilename = 'C:\\Users\\swapnily\\Desktop\\Auto\\project_bootscrap_version7\\%s.readerslist'%filename

   set_file_via_ftp('get',remotefilename,localfilename,ssh)
      
   with open ('%s.readerslist'%filename, 'rb') as fp:
      articles_to_display = pickle.load(fp)

   return articles_to_display

def reset_reader_list(filename,ssh):
   '''Reset reader list with empty file'''
   articles_to_display = []
   remotefilename = '/usr/src/scrapper/%s.readerslist'%filename
   localfilename = 'C:\\Users\\swapnily\\Desktop\\Auto\\project_bootscrap_version7\\%s.readerslist'%filename
   
   with open ('%s.readerslist'%filename, 'wb') as rrp:
      pickle.dump(articles_to_display,rrp)
   set_file_via_ftp('put',localfilename,remotefilename,ssh)
         
def read_from_server(IP,username,password):
   '''Connect to server and fetch readerlist'''
   
   ssh = connect_to_server(IP,username,password)

   display_articles = []
   
   for filename in masterlist.lofiles:
      
      articles_to_display = get_reader_list(filename,ssh)
      if len(articles_to_display) > 0:
         for link in articles_to_display:
            display_articles.append(link)     
         reset_reader_list(filename,ssh)
         
   return display_articles

#Begin from here

IP = '10.107.47.155'
username = 'root'
password = 'mybjo@01'

display_articles = read_from_server(IP,username,password)

#if len(display_articles) > 0:
 #  learner.remove_similar(display_articles)


if len(display_articles) > 0:
    #with open ('master.readerslist', 'wb') as mrp:
     #       pickle.dump(display_articles,mrp)
    #learn_recommend(display_articles)
    for link in display_articles:
        webbrowser.open(link)
else:
    print("No articles to display, check after sometime!!")
    time.sleep(5)

