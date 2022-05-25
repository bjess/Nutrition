import requests

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/479101/information"

headers = {
	"X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
	"X-RapidAPI-Key": "19553eff50mshef4a13bcaed815ep1e9b9ejsn985a01818a57"
}

response = requests.request("GET", url, headers=headers)

print(response.text)
