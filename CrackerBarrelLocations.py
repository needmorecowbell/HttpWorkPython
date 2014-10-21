import urllib
import re

f = open('addresses.txt', 'r+')

states= ['alabama','arizona','arkansas','colorado','connecticut','delaware','florida','georgia','idaho',
         'illinois','indiana','iowa','Kansas','Kentucky','louisiana','maine','maryland','massachusetts',
         'michigan','minnesota','mississippi','missouri','montana','nebraska','new-hampshire','new-jersey',
         'new-mexico','new-york','north-carolina','south-carolina','south-dakota','tennessee','texas','utah',
         'virginia','west-virginia','wisconsin']

for state in states:
    f.write("##################### "+ state+" #######################\n")
    htmlfile= urllib.urlopen("http://www.crackerbarrel.com/locations-and-hours/browse-locations/"+state+"/")
    #reg= '<div class="store"> </div>'
    reg= '<b>(.+?)</b>'
    pattern= re.compile(reg)

    htmltext= htmlfile.read()


    
    trimmed=re.findall(pattern, htmltext)

    for x in trimmed:
        f.write(x)
        f.write("\n\n")


