import requests
from random import randint

i = randint(1, 5)
r =requests.get('http://widgets-widget:3000/widget/' + str(i))
t = r.text
print(t)

i = randint(1, 5)
r =requests.get('http://widgets-quantity:3001/quantity/' + str(i))
t = r.text
print(t)

i = randint(1, 5)
r =requests.get('http://widgets-warehouse:3002/warehouse/' + str(i))
t = r.text
print(t)
