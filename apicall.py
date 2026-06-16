import os
import requests
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.environ.get('CLIENT_ID')

url = f'https://api.nytimes.com/svc/mostpopular/v2/emailed/7.json?api-key={CLIENT_ID}'

response = requests.get(url)

response_data = response.json()

results = response_data.get('results', [])
for i, article in enumerate(results, 1):
    print(f"{i}. {article.get('title')}")
    print(f"   URL: {article.get('url')}\n")
