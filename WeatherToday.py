import urllib
import re

curTempStr= '<p class="myforecast-current-lrg">(.+?)</p>'
locStr='<p class="current-conditions-location">(.+?)</p>'
htmlfile= urllib.urlopen("http://forecast.weather.gov/MapClick.php?lat=40.3226541152963&lon=-80.0391172373698&site=all&smap=1#.U55ZH_ldWPU")
reg= curTempStr
curTempPat= re.compile(reg)
reg=locStr
locPat= re.compile(reg)
htmltext= htmlfile.read()

tempList= re.findall(curTempPat,htmltext)
temp= ''.join(tempList)

locList= re.findall(locPat, htmltext)
loc= "".join(locList)


print temp
print loc