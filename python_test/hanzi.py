# encoding: UTF-8
import re
                               
test_name_1 = u'一二三四五六七八九十a' #长度为21字节，不符合
test_name_2 = u'戊In厦门'
                               
def check_name_format(name):
    re_name = ur'^([a-zA-Z][\w]{2,19}|[\u4e00-\u9fa5]{1,10}|[\u4e00-\u9fa5a-zA-Z][\u4e00-\u9fa5\w]{2,19})$'
    pattern = re.compile(re_name)
    match = pattern.match(name)
    if match:
        return True if len(name) + zh_count(name) <= 20 else False
    else:
        return False
                               
def zh_count(string):
    re_zh = ur'[\u4e00-\u9fa5]'
    pattern = re.compile(re_zh)
    hanzi=pattern.findall(string)
    for word in hanzi:
	print word
    return len(pattern.findall(string))
                               
print check_name_format(test_name_1)
print check_name_format(test_name_2)