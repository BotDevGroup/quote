
import requests

response = requests.get('https://andruxnet-random-famous-quotes.p.mashape.com/?cat=movies',headers={
  "X-Mashape-Key": "BEjqsVLNGDmshmQ0ZxP0TC6j7wfDp1tlihvjsnUhhELDOJA7f5",
  "Content-Type": "application/x-www-form-urlencoded",
  "Accept": "application/json"
})
r = response.json()

print(r['quote'])
