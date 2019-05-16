import re
str = "winnPop=window.open('https://www.findsgjobs.com/display-job/10149/Royal-Sporting-House---Sales-Associate.html?searchId=1&page=2','JobDetail', 'height=500,width=1300,scrollbars=1');winnPop.focus();"
i = 0

for m in re.finditer("'", str):
    if i < 2:
        print("' found", m.start() , m.end())

    i+=1

print re.findall(r'"([^"]*)"', str)
ss = re.findall(r"'([^']*)'", str)
print ss[0]
		

'''
substring1 = "'"
substring2 = "'"
s = strs
my_string = s[(s.index(substring1)+len(substring1)):s.index(substring2)]
print my_string
'''

#http://stackoverflow.com/questions/2076343/extract-string-from-between-quotations
#http://stackoverflow.com/questions/22735440/extract-a-string-between-double-quotes
#http://stackoverflow.com/questions/19675760/extracting-strings-in-python-in-either-single-or-double-quotes
#https://jefworks.wordpress.com/category/code/python/string-methods/
#http://daringfireball.net/2010/07/improved_regex_for_matching_urls
#http://pythex.org/
#https://github.com/tartley/python-regex-cheatsheet/blob/master/cheatsheet.rst
