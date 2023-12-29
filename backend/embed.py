import requests
import json

url = "https://api.cohere.ai/v1/embed"


animal_names = ["Elephant", "Tiger", "Kangaroo", "Penguin", "Giraffe", "Dolphin", "Eagle", "Panda", "Lion", "Turtle"]
inanimate_objects = ["Chair", "Laptop", "Clock", "Bicycle", "Teapot", "Book", "Lamp", "Painting", "Shoe", "Glasses"]
countries = ["Brazil", "Japan", "Canada", "Kenya", "Australia", "Germany", "India", "Mexico", "South Korea", "Italy"]

documents = animal_names + inanimate_objects + countries


payload = {
    "texts": documents,
    "truncate": "END"
}

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer fNVdfxXASbB8bBp7kwecELHp3BIqj26A3S0ha8Xg"
}

vectors = json.loads(requests.post(url, json=payload, headers=headers).text)['embeddings']

embeddings = {}

for vector_index in range(len(vectors)):
    embeddings[documents[vector_index]] = vectors[vector_index]

print(embeddings)
