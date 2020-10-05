import requests
import datetime
from Parallelizer import make_parallel


def make_api_call(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {}


list_of_urls = [f"https://jsonplaceholder.typicode.com/posts/{post_id}" for post_id in range(1, 201)]

results = []
st = datetime.datetime.now()
for url in list_of_urls:
    results.append(make_api_call(url))
print(f'Non Parallelized took -- {datetime.datetime.now() - st}')

st = datetime.datetime.now()
results = make_parallel()(make_api_call)(list_of_urls)
print(f'Parallelized took -- {datetime.datetime.now() - st}')
