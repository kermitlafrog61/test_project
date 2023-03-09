import requests

def get_html(url: str) -> str:
    return requests.get(url).text

def pain():
    return 'This world shall know pain\nAllmighty push'