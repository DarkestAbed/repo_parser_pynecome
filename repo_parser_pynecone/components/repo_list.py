import reflex as rx
import requests
import logging

def full_repo_retrieval(base_url: str) -> rx.Component:
    get_url = f"{base_url}/get-local-repos"
    request = requests.request(method="GET", url=get_url)
    logging.info(request)
    logging.info(request.text)
    return request.text


# def 