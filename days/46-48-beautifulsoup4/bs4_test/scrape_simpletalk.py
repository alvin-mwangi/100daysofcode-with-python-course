import bs4
import requests
import os

with open("simpletalkhome.html", encoding='utf-8') as f:
    data = f.read()
    soup = bs4.BeautifulSoup(data, 'html.parser')

    # print(soup.find_all('li')[0])

    first_product = soup.ul.li.ul.find_all('li')[0]
    first_product_name = first_product.a.string

    first_product_items = first_product.find_all('li')
    # # print(first_product_items)

    print(f"Here are the tools available for {first_product_name}:")
    for item in first_product_items:
        print(item.string)
