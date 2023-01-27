#import urllib.parse
#//import urllib.request
#//params = urllib.parse.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
#//f = urllib.request.urlopen("http://www.musi-cal.com/cgi-bin/query?%s" % params)
#//print(f.read())

try:
	from googlesearch import search
except ImportError:
	print("No module named 'google' found")

# to search
query = "Geeksforgeeks"

for j in search(query, tld="co.in", num=10, stop=10, pause=2):
	print(j)
