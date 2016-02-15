import urllib # URL Handling library for Python. Very High level. https://docs.python.org/2/library/urllib.html#module-urllib

print 'GET Request'
url = raw_input("Type in a URL. Include Protocol. (eg. http://www.example.com:")
GETurl = urllib.urlopen(url) #This is not the ideal urllib method to use. FancyURLopener or URLopener are better suited as they support http/ ftp etc.
print ' Sending GET request ' + url 
print '***************'
print GETurl.read()