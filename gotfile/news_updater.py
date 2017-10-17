import scrapper
import masterlist
import utils
import time

#from apscheduler.schedulers.blocking import BlockingScheduler
#sched = BlockingScheduler()
#@sched.scheduled_job('cron', day_of_week='mon-fri', hour=5)
#@sched.scheduled_job('interval', hours=4)

def news_updater():
    master_list = []
    master_list = utils.load_file('master.readerslist')
    old_count = len(master_list)        
    for filename in masterlist.lofiles:
        articles_to_display = []
        articles_to_display = scrapper.scrap_url_with_rules_and_data(filename)
        master_list = master_list + articles_to_display

    utils.dump_file('master.readerslist',master_list)
    print("Last ran at = %s, update %s new articles "%(time.ctime(),old_count - len(master_list)))

news_updater()
#sched.start()

