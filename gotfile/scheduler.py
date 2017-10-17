

from apscheduler.schedulers.background import BackgroundScheduler
#BlockingScheduler #, 
sched = BackgroundScheduler()#BlockingScheduler() #

@sched.scheduled_job('interval', seconds=5)
def timed_job():
    print('This job is run every 10 seconds.')

#@sched.scheduled_job('cron', day_of_week='mon-fri', hour=10)
#def scheduled_job():
#    print('This job is run every weekday at 10am.')

#sched.configure(options_from_ini_file)
sched.start()
