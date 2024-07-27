import requests
from random import choice
from pyfiglet import figlet_format
from termcolor import colored

header = figlet_format("Dad Jokes 3000")
header = colored(header, color="magenta")
print(header)

user_input = input("What would you like to search for? ")
url = "https://icanhazdadjoke.com/search"

res = requests.get(
	url, 
	headers={"Accept": "application/json"},
	params={"term": user_input}
).json()

count = res["total_jokes"]
results = res["results"]

if count > 1:
	print(f"There are {count} jokes with the word '{user_input}', here's one:")
	print(choice(results)["joke"])
elif count == 1:
	print(f"There is one joke with the word {user_input}. Here it is:")
	print(results[0]["joke"])
else:
	print(f"There are no jokes with the word '{user_input}'")














