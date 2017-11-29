import config
from robobrowser import RoboBrowser
import re

br = RoboBrowser()
br.open("https://e-hentai.org/bounce_login.php")
form = br.get_form()
form ['UserName'] = config.DATACOUP_NAME
form ['PassWord'] = config.DATACOUP_PASS
br.submit_form(form)
br.open("https://e-hentai.org/hentaiathome.php")
src = str(br.parsed()) #store all the htmlpage into src

start = '<td style="font-weight:bold; color:green">'
end = '</td>'

Status = re.search('%s(.*)%s' % (start, end), src).group(1)
print(Status)

#Your IP address has been temporarily banned for excessive pageloads which indicates that you are using automated mirroring/harvesting software. The ban expires in 33 minutes and 26 seconds
