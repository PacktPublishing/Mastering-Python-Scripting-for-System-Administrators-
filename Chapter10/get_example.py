import http.client

con_obj = http.client.HTTPSConnection("www.imdb.com")
con_obj.request("GET", "/")
response = con_obj.getresponse()
print("Status: {}".format(response.status))

read_data = response.read(1000)
print(read_data)
con_obj.close()
