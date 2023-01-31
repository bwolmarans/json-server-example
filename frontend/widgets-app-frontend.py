import requests
from random import randint

i = randint(1, 5)
r =requests.get('http://127.0.0.1:3000/quantity/' + str(i))
t = r.text
print(t)

i = randint(1, 5)
r =requests.get('http://127.0.0.1:3001/widget/' + str(i))
t = r.text
print(t)

i = randint(1, 5)
r =requests.get('http://127.0.0.1:3002/warehouse/' + str(i))
t = r.text
print(t)
