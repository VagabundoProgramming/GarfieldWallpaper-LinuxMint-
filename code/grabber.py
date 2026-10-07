import requests
from os import getcwd
from bs4 import BeautifulSoup

IMG_PATH: str = getcwd()+"/imgs"
COMIC_CLASS: str = "Comic-module-scss-module__3szrOa__comic__image Comic-module-scss-module__3szrOa__comic__image_isStrip"

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
})


def _search_link(html_source: str) -> str:
    html_substring = html_source[html_source.find(COMIC_CLASS):]
    if html_substring == "":
        return

    html_substring = html_substring[html_substring.find("src=\"") + len("src=\""):]
    return html_substring[:html_substring.find("?")]

def get_today_comic() -> None:
    response = session.get("https://www.gocomics.com/garfield/")
    soup = str(BeautifulSoup(response.text, "html.parser"))

    url = _search_link(soup)

    data = session.get(url).content

    f = open(f"{IMG_PATH}/GarfToday.png","wb")
    f.write(data)
    f.close()
    return

if __name__ == "__main__":
    get_today_comic()