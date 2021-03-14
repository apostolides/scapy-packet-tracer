import requests as r

def country_from_ip(ip):
    country_api_endpoint = f"https://ipapi.co/{ip}/json/"
    response = r.get(country_api_endpoint)
    payload = None
    if response.status_code == 200:
        payload = response.json()
    return payload