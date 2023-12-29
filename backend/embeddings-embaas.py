import requests
# from sklearn.metrics.pairwise import cosine_similarity

headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer DF71DE45657014710C4B680C9C1024A7'}

animal_names = ["Elephant", "Tiger", "Kangaroo", "Penguin", "Giraffe", "Dolphin", "Eagle", "Panda", "Lion", "Turtle"]
inanimate_objects = ["Chair", "Laptop", "Clock", "Bicycle", "Teapot", "Book", "Lamp", "Painting", "Shoe", "Glasses"]
countries = ["Brazil", "Japan", "Canada", "Kenya", "Australia", "Germany", "India", "Mexico", "South Korea", "Italy"]

documents = animal_names + inanimate_objects + countries

data = {
    'texts': documents,
    'model': 'bge-large-en-v1.5',
}

response = requests.post("https://api.embaas.io/v1/embeddings/", json=data, headers=headers)
vectors = response.json()["data"]

embeddings = {}

for vector_index in range(len(vectors)):
    embeddings[documents[vector_index]] = vectors[vector_index]['embedding']

print(embeddings)