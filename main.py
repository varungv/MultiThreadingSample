from Parallelizer import make_parallel
import requests


def sample_function(post_id):
    """
        Just a sample function which would make dummy API calls
    """

    url = f"https://jsonplaceholder.typicode.com/comments?postId={post_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return {}


list_of_post_ids = list(range(1, 20))

# Serial way of calling the function
results = []
for post_id in list_of_post_ids:
    res = sample_function(post_id)
    results.append(res)

# Paralleized way of calling the function
results = make_parallel(sample_function)(list_of_post_ids)