import http.client

con_obj = http.client.HTTPSConnection("www.imdb.com")
con_obj.request("GET", "/")

response = con_obj.getresponse()
headers_list = response.getheaders()

print("Headers: {}".format(headers_list))
