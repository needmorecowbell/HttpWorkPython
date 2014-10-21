import urllib
import re

htmlfile= urllib.urlopen("http://www.quotationspage.com/qotd.html")
reg= '<dt class="quote">(.+?)</dt>'
pattern= re.compile(reg)
htmltext= htmlfile.read()
trimmed= re.findall(pattern,htmltext)

quote= ''.join(trimmed)

quote=quote[quote.index(">")+1: quote.index("</a>")]

print quote