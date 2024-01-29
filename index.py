
import requests

URL = "GET /v1/vehicles/usa/all"

PARAMS = {'aircraft', 'ground', 'naval', 'coastal'}


r = requests.get(url = URL, params = PARAMS)


data = r.json()

https://github.com/X-rays5/wt-api/blob/master/readme.md


#nation = input('What nation are you playing?\n')

#tank = input('What tank are you using?\n')

#problem_tank = input('What tank is giving you issues\n')

#Array1 = [nation,tank,problem_tank]


#print(Array1)
print(data)