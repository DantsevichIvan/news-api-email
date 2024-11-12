import requests

api_key = "c9fc3a35460342bb85435c046112b51f"
url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={api_key}"

request = requests.get(url)
content = request.json()
print(content["articles"])
