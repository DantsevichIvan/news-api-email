import requests
import os
from send_email import send_email

api_key = os.getenv("NEWS_API_KEY")
url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={api_key}"

request = requests.get(url)
content = request.json()

body = ""
for article in content["articles"]:
    if article["title"] is not None and article["description"] is not None:
        body = body + article["title"] + "\n" + article["description"] + "\n" + article["url"] + 2 * "\n"

body = body.encode("utf-8")
send_email(message=body)
