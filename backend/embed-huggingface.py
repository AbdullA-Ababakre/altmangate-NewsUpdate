
animal_names = ["Elephant", "Tiger", "Kangaroo", "Penguin", "Giraffe", "Dolphin", "Eagle", "Panda", "Lion", "Turtle"]
inanimate_objects = ["Chair", "Laptop", "Clock", "Bicycle", "Teapot", "Book", "Lamp", "Painting", "Shoe", "Glasses"]
countries = ["Brazil", "Japan", "Canada", "Kenya", "Australia", "Germany", "India", "Mexico", "South Korea", "Italy"]

documents = animal_names + inanimate_objects + countries


from sentence_transformers import SentenceTransformer
sentences_1 = documents
model = SentenceTransformer('BAAI/bge-large-zh-v1.5')
embeddings_1 = model.encode(sentences_1, normalize_embeddings=True)
print(embeddings_1)
