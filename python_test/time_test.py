from datetime import *
import time
import datetime  

print 'date.max:', date.max
print 'date.min:', date.min
print 'date.today():', date.today()-datetime.timedelta(days =10) 
print 'date.fromtimestamp():', date.fromtimestamp(time.time())