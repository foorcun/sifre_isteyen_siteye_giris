from bs4 import BeautifulSoup
import urllib.request
import webbrowser
import requests
from requests.auth import HTTPBasicAuth
url='https://girisv3.itu.edu.tr/Login.aspx?subSessionId=3835c24f-245c-4e37-bcfd-bc4ea5f6d779&currentURL=http%3A%2F%2Fuzay.sis.itu.edu.tr%2Flogin%2Findex.php'
#login isteyen url
url_auth=requests.get(url, auth=HTTPBasicAuth('kamacif', 'UYsKG983BW'))
##login denemesi yapar dondurdugu 200 ise giriş yapılmştr


url_pin="http://ssb.sis.itu.edu.tr:9000/pls/PROD/twbkwbis.P_WWWLogin/?SessionId=a14fa7d5-dc39-4f69-b2da-3c2695f46c9b" ##login basarılı olunca yonlendırılen url
webbrowser.open(url_pin)

