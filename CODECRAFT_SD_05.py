import requests
from bs4 import BeautifulSoup
import csv

def scrape_products(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    products = []

    # Example for a generic e-commerce site (update selectors for your target site)
    for item in soup.select('.product'):  # Change '.product' to the actual product container selector
        name = item.select_one('.product-title')  # Change to actual selector
        price = item.select_one('.product-price')  # Change to actual selector
        rating = item.select_one('.product-rating')  # Change to actual selector
        products.append({
            'name': name.text.strip() if name else '',
            'price': price.text.strip() if price else '',
            'rating': rating.text.strip() if rating else ''
        })
    return products

def save_to_csv(products, filename='products.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'price', 'rating'])
        writer.writeheader()
        for product in products:
            writer.writerow(product)

def main():
    url = input('Enter the URL of the e-commerce page to scrape: ')
    products = scrape_products(url)
    save_to_csv(products)
    print(f'Scraped {len(products)} products and saved to products.csv')

if __name__ == '__main__':
    main()
