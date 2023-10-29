import requests

def get_categories():
    request = requests.get('https://api.escuelajs.co/api/v1/categories')
    categories = request.json()
    for category in categories:
        print('Category: ', category['name'])