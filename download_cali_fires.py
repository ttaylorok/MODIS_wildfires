import requests
from requests.auth import HTTPBasicAuth
files = open("cali_2018_links_june01-dec31.txt",'r')
from requests.auth import HTTPDigestAuth
#output = open('output.txt', 'wb')

for line in files:
    print(line)
    link = line.strip()
    name = link[(link.rfind("/")+1):]
    out = open("cali_2018_data/"+name,'wb')
    r = requests.get(link, allow_redirects=True,auth=HTTPDigestAuth('txtimmer87', 'san!nanp4smS'))
    out.write(r.content)
    out.close()
    break

files.close()
