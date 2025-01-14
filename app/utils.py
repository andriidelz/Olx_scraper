import os
import json
from datetime import datetime
import logging

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        logging.info(f"Directory created: {path}")
    else:
        logging.info(f"Directory already exists: {path}")

def json_serializable(obj):
    try:
        return json.dumps(obj)
    except TypeError as e:
        logging.error(f"Error serializing object: {e}")
        return str(obj)

def parse_price(price_str):
    if price_str:
        return ''.join(filter(str.isdigit, price_str))
    return None

def extract_images(image_urls):
    valid_images = [url for url in image_urls if url.startswith('http')]
    return valid_images

def format_url(url):
    if not url.startswith('http'):
        url = 'http://' + url
    return url

