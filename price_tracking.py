import requests
from bs4 import BeautifulSoup

URL = (
    "https://www.amazon.com/Stewarts-Cream-Soda-12oz-bottles"
    "/dp/B072FW8BDT/ref=sr_1_1?crid=3GE56HV1BXGUY&dchild=1&keywords=cream+soda+"
    "stewarts&qid=1612080523&sprefix=cream+soda+stew%2Caps%2C304&sr=8-1"
)
URL_EBAY = (
    "https://www.ebay.com/itm/STEWARTS-CREAM-SODA-2-Unit-s-Each-Unit-Is"
    "-4-X-355ML/402222633167?hash=item5da65650cf:g:1KwAAOSw4pJd5G3J"
)

# print(f"URL: {URL}")
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
}

print(f"headers: {headers}")

page = requests.get(URL_EBAY, headers=headers)

# print(f"page: {page}")


html_content = BeautifulSoup(page.content, "html.parser")

# print(f"html_content: {html_content}")
# print(f"html_content type: {type(html_content)}")
# title = html_content.find(id="productTitle")

title = html_content.find(id="itemTitle").get_text()
price = html_content.find(id="prcIsum").get_text()
converted_price = float(price[-5:])


print(title.strip())
print(converted_price)

