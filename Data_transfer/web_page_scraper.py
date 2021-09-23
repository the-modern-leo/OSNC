import requests

URL = "https://wiki.utah.edu/display/NetOpSup/U+of+U+Network+Locations"
page = requests.get(URL)

print(page.text)
