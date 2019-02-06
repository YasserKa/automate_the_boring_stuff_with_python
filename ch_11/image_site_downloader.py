import os
import requests
import bs4

url = 'https://imgur.com/search?q=sun'
dirName = 'images'

os.makedirs(dirName, exist_ok=True)

res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)

images = soup.select('img')

for image in images:
    src = 'http://' + image.get('src')[2:]
    baseName = os.path.basename(src)
    res = requests.get(src)
    print('Downloading ' + src)
    fileStream = open(os.path.join(dirName, baseName), 'wb')
    for chunk in res.iter_content(100000):
        fileStream.write(chunk)
    fileStream.close()
print('Done')
