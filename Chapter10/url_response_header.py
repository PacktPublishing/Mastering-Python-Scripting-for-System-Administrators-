import urllib.request

x = urllib.request.urlopen('https://www.imdb.com/')
print(x.info())

