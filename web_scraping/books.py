from bs4 import BeautifulSoup as bs
import requests

url = "https://estivalet.github.io/static-testing-sites/bookdepository"
response = requests.get(url)
html = response.content

soup = bs(html, 'lxml')

book_items = soup.find_all("div", class_="book-item")

for book_item in book_items:
  print("Title: " + book_item.find("h3").get_text(strip=True))
  print("Author: " + book_item.find("p", class_="author").get_text(strip=True))
  print("Published on: " + book_item.find("p", class_="published").get_text(strip=True))
  print("Format: " + book_item.find("p", class_="format").get_text(strip=True)) 
  original_price = book_item.find("span", class_="rrp")
  current_price = book_item.find("p", class_="price")
  if not current_price:
    print("Price: Out of Stock \n") 
  else:
    if original_price:
      print("Original Price: $" + original_price.get_text(strip=True).split('R$')[1])
      print("Current Price: " + current_price.get_text(strip=True).split('R$')[0] + "\n") 
    else:
      print("Price: " + current_price.get_text(strip=True) + "\n") 


  


