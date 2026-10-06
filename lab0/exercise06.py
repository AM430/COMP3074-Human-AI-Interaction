"""6.Write code to access a webpage and extract some text from it. Print it to the console. For
example, access a weather site and extract the forecast top temperature for your town or
city today."""

from urllib import request

from bs4 import BeautifulSoup

# url = "https://example.com"
# html = request.urlopen(url).read().decode("utf-8")
# print(html)

# text = BeautifulSoup(html, "html.parser").get_text()
# print(text)

url = "https://example.com"
html = request.urlopen(url).read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
# print(soup.prettify())
title = soup.find("title")
# print(title.get_text())
# print(soup.title)
# print(soup.title.text)
if title is not None:
    print(title.get_text())
else:
    print("No title tag found.")
