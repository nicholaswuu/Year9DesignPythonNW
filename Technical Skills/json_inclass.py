import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")
todos = json.loads(response.text)

print(todos[0]["userId"])