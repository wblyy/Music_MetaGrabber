 # encoding: UTF-8
import re
import urllib2
import urllib
import time
from mydb import Tiedb
tiebadb = Tiedb()

print tiebadb.get_album("青花瓷","周杰伦")[0]
