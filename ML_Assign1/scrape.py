import urllib
import json
import csv
import collections

url = "https://api.coinmarketcap.com/v1/ticker/?convert=CAD"
response = urllib.urlopen(url).read()
data = json.loads(response, object_pairs_hook=collections.OrderedDict)
print data

outputFile = open("cryptoprices.csv", 'wb')

output = csv.writer(outputFile)
output.writerow(data[0].keys())

for row in data:
    output.writerow(row.values())