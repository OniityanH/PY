import config
from robobrowser import RoboBrowser
import re

br = RoboBrowser()
br.open("https://www.e.com/")
form = br.get_form()
form ['email'] = config.DATACOUP_NAME
form ['pass'] = config.DATACOUP_PASS
br.submit_form(form)
src = str(br.parsed()) #store all the htmlpage into src

start = '<span class="_1vp5">'
end = '</span>'

res = re.search('%s(.*)%s' % (start, end), src).group(1)
print('234')
print(res)