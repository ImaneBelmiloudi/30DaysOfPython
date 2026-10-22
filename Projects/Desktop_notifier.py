from plyer import notification
import time
from topnews import topStories

# path to notification window icon
ICON_PATH = "put full path to icon image here"

# fetch news items
newsitems = topStories

# initialise the d-bus connection
notification.init("News Notifier")

# create Notification object
n = notification.Notification(None, icon = ICON_PATH)

# set urgency level
n.set_urgency(notification.URGENCY_NORMAL)

# set timeout for a notification 
n.set_timeout(10000)

for newsitem in newsitems :

    # update notification data for Notification object
    n.update(newsitem['title'], newsitem['description'])

    # show notification on screen
    n.show()

    #short delay between notifications
    time.sleep(15)