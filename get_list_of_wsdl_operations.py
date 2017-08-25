import urllib2
import lxml.html

url = "http://www.webservicex.com/globalweather.asmx?wsdl"

web = urllib2.urlopen(url).read()
 
namespaces = {"ns": "http://schemas.xmlsoap.org/wsdl/"}
 
root = lxml.etree.fromstring(web)
 
print
 
print "Root tag:"
print(root.tag)
 
print
 
print "Count of elements under root tree:"
print(len(root))
 
print
print
 
print "List of elements based on XPath Expression:"
list1 = root.xpath('//ns:operation/@name', namespaces=namespaces)
print list1
print len(list1)
 
list2 = []
 
for i in list1:
    if i not in list2:
        list2.append(i)
 
print
print "List of unique WS operations"
print list2
print len(list2)
 
print
print "Print list of unique WS operations"
for i in list2:
    print i
