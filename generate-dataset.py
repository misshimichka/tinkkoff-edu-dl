import requests
import bs4


address = "https://www.allfreenovel.com/Page/Story/42873/page-1-of-Fahrenheit-451/"
file = open("Fahrenheit-451.txt", mode="wt")
for i in range(1, 51):
    response = requests.get(address + str(i))
    soup = bs4.BeautifulSoup(response.content, "html.parser")

    text_tags = soup.find_all("p", {"class": "storyText story-text"})
    for tag in text_tags:
        file.write(tag.text)
        file.write("\n")
file.close()
