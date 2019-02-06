import os
import requests
import bs4

# sanatizing the href is needed before downloading
url = 'https://play2048.co/'
dirName = 'images'

os.makedirs(dirName, exist_ok=True)

res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)

images = soup.select('a')

for image in images:
    src = image.get('href')
    baseName = os.path.basename(src)
    res = requests.get(src)
    if res.status_code == requests.codes.ok:
        pass
    try:
        res.raise_for_status()
    except Exception:
        print(src+' was not downlaoded')

    print('Downloading ' + src)
    fileStream = open(os.path.join(dirName, baseName), 'wb')
    for chunk in res.iter_content(100000):
        fileStream.write(chunk)
    fileStream.close()
print('Done')
