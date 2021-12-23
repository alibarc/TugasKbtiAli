url = 'https://www.gutenberg.org/files/2701/2701-h/2701-h.htm'

import requests

r = requests.get(url)
type(r)

html = r.text
print(html)

