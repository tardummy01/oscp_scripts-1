import httplib #Lower level HTTP library. https://docs.python.org/2/library/httplib.html 

url = raw_input("Type in a URL. Eg (www.example.com): ")
conn = httplib.HTTPSConnection(url) #Sets HTTP Connection to user inputed string. 
conn.request("GET", "/") #Sets HTTP Request Type

response = conn.getresponse() #Gets Response. 



print "Status: " + str(response.status) +  ", Reason: " + str(response.reason)
print "Body"
print response.read()

