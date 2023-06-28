import random
import re
import time
#import pandas
import requests
from bs4 import BeautifulSoup
#from pandas import ExcelWriter

def get_html(url, params=None):
    """ получение кода страницы """
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0)"
    }
    html = requests.get(url, headers=headers, params=params)
    return html

print(get_html("https://www.avito.ru/sankt-peterburg/telefony/mobilnye_telefony/apple/iphone_13-ASgBAgICA0SywA3svcgBtMANzqs5sMENiPw3?cd=1"))
