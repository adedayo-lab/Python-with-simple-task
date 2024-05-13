# program that downloads img file from the
# Net using its url

import random
import urllib.request

def download_web_image(url):
    mame = random.randomrange(1, 1999)
    full_name =str(name) + ".jpg"
    urllib.request.urlretrive(url, full_name)


input = download_web_image(" ")
