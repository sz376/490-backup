import requests
import os
import json
from os.path import join, dirname
from dotenv import load_dotenv
import json

spoonacular_key = '834e65a549cc4a41a1b1afbfb59cb26e'
food = 'burger'
url = f"https://api.spoonacular.com/recipes/complexSearch?query={food}&apiKey={spoonacular_key}"
response = requests.get(url)
json_body = response.json()
rid = json_body["results"][0]["id"]
print(rid)
url = f"https://api.spoonacular.com/recipes/{rid}/information?apiKey={spoonacular_key}"
response = requests.get(url)
json_body = response.json()
stuff=[]

for i in range(len(json_body["extendedIngredients"])):
    stuff.append(json_body["extendedIngredients"][i]["original"])
    '''
print(json_body["extendedIngredients"]["original"])
'''
print(stuff)
