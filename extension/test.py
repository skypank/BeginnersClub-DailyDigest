# Import smtplib for the actual sending function
import smtplib

def publish_post(articles):
    #for link in articles:
    publish ="\n".join(articles)
    #print(publish)
    receivers = 'gedi892lizi@post.wordpress.com'
    sender= ['skypank@gmail.com']
    message = 'From: Beginners<skypank@gmail.com>'+'\n' \
    'To: BeginnersClub forum <gedi892lizi@post.wordpress.com>'+'\n' \
    'Subject: Daily Digest'+'\n' \
    '\n'+publish+'\n'
       

    try:
        s = smtplib.SMTP(host='smtp.gmail.com', port='587')
        s.starttls()
        s.login('skypank@gmail.com','qytaihcksorlgien')
        s.sendmail(sender,receivers,message)
        print ("Successfully sent email")
    except Exception as e:
        print ("Error: unable to send email")


#publish_post()
