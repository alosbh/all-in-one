import urllib
try:
    url = "https://www.google.com"
    urllib.urlopen(url)
    status = "Connected"
except Exception as e:
    status = "Not connected"
    print (status)
    print(type(e).__name__)
if status == "Connected":
    print("do stuff")