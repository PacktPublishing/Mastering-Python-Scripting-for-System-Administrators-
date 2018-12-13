import http.client
import json

con_obj = http.client.HTTPSConnection('www.httpbin.org')

headers_list = {'Content-type': 'application/json'}

post_text = {'text': 'Hello World !!'}
json_data = json.dumps(post_text)

con_obj.request('POST', '/post', json_data, headers_list)

response = con_obj.getresponse()
print(response.read().decode())
