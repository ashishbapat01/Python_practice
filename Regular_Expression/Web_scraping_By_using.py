import re,urllib
import urllib.request
sites="google.com ".split()
print(sites)
for s in sites:
	print("Searching...",s)
	u=urllib.request.urlopen("https://github.com/ashishbapat01/ashishbapat01"+s+".com")
	text=u.read()
	title=re.findall("<title>.*</title>",str(text),re.I)
	print(title[0])