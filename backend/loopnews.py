from datetime import datetime, timedelta
import time
import json
import requests


def embed(summary):
    headers = {'Content-Type': 'application/json',
               'Authorization': 'Bearer DF71DE45657014710C4B680C9C1024A7'}

    data = {
        'texts': [summary],
        'model': 'bge-large-en-v1.5',
    }

    response = requests.post("https://api.embaas.io/v1/embeddings/", json=data, headers=headers)
    vectors = response.json()["data"]

    return vectors[0]['embedding']


def get_articles():
    url = 'https://api.newscatcherapi.com/v2/search'

    headers = {
        "x-api-key": "AZTYYrrZZtMDXsJ9u44fMe2LaPeDPYm95qX3fWcaV1E"
    }

    # set page_size = 1 to see structure of the response. Then change back to 1000
    params = {"q": "Sam Altman, fired, OpenAI",
              "from": (datetime.now() - timedelta(seconds=60)).strftime("20%y/%m/%d %H:%M:%S"),
              "to": datetime.now().strftime("20%y/%m/%d %H:%M:%S"),
              "page_size": 10}

    response = json.loads(requests.get(url, headers=headers, params=params).text)
    vectorized_response = []

    if response['status'] != 'No matches for your search.':
        for article in response['articles']:
            try:
                vectorized_response.append({"title": article['title'],
                                            "excerpt": article['excerpt'],
                                            "published_date": article['published_date'],
                                            "link": article["link"],
                                            "vector": embed(article['excerpt'])})

            except:
                print("shitty article:", article)

    return vectorized_response


while True:
    print(get_articles())
    time.sleep(60)