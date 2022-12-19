import csv
import requests

nbdownload = 0

with open('CSV LINK HERE', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:

        url = row['LINK HEADER']
        name = row['NAME HEADER']

        print(url, name)

        r = requests.get(url, allow_redirects=True, stream= True, headers={'User-agent': 'Mozilla/5.0'})
        open(name, 'wb').write(r.content)

        nbdownload = nbdownload + 1
        print("Download done")

print(f'Download finish with {nbdownload} entries')      