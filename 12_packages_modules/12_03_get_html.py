'''
In 3 lines of code, fetch the HTML text from codingnomads' main page
and print it to your console.

TIP:
- if you wonder what to use, google something like
    "most popular python package"
- if you run into encoding/decoding errors, you're experiencing something
    very common. head over to SO and find a solution!

'''

import urllib.request

fp = urllib.request.urlopen("http://codingnomads.co")
page = fp.read()

page = page.decode("utf8")
fp.close()

print(page)

'''
import requests
url = requests.get("https://codingnomads.co/")
htmltext = url.text
print(htmltext)
'''

