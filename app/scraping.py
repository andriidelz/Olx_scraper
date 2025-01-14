import requests
from bs4 import BeautifulSoup
from .crud import create_listing
from .models import SessionLocal

def scrape_olx():
    db = SessionLocal()
    url = "https://www.olx.ua/uk/"
    for page_num in range(1, 6): 
        response = requests.get(f"{url}?page={page_num}")
        soup = BeautifulSoup(response.text, 'html.parser')
        
        listings = soup.find_all('div', class_='offer-wrapper')
        
        for listing in listings:
            title = listing.find('strong').get_text(strip=True)
            description = listing.find('div', class_='space').get_text(strip=True)
            views = int(listing.find('div', class_='views').get_text(strip=True).split()[0])
            service_type_elem = listing.find('div', class_='service-type')
            service_type = service_type_elem.get_text(strip=True) if service_type_elem else "Unknown"
            listing_url = listing.find('a')['href']

            create_listing(db, title, description, views, service_type, listing_url)

    db.close()
