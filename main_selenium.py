from typing import List
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os
import time
import spotipy

load_dotenv()

BILLBOARD_BASE_URL = "https://www.billboard.com/charts/hot-100"
SPOTIFY_CLIENT_ID = os.getenv("CLIENT_ID")
SPOTIFY_CLIENT_SECRET_ID = os.getenv("CLIENT_SECRET_KEY")


class MusicTimeVehicle:
    """
    A class to construct Billboard chart URLs for a given date and scrape song titles.

    Attributes:
        my_search_date (str): The date of the chart in format 'YYYY-MM-DD'.
    """

    def __init__(self, my_search_date: str) -> None:
        """
        Initializes the MusicTimeVehicle with a specific chart date.

        Args:
            my_search_date (str): The date in format 'YYYY-MM-DD'.
        """
        self.my_search_date = my_search_date

    def build_url(self) -> str:
        """
        Builds the full Billboard chart URL based on the provided date.

        Returns:
            str: A complete URL to the Billboard chart for the given date.
        """
        return f"{BILLBOARD_BASE_URL}{self.my_search_date}"

    @staticmethod
    def choose_srap_date() -> str:
        """
        Prompts the user to input a date in the required format.

        Returns:
            str: The user-provided date in format 'YYYY-MM-DD'.
        """
        return input("Please give me the date with format -> '/YYYY-MM-DD/': ")

    def selenium_web_connector(self, search_url: str) -> List[str]:
        """
        Uses Selenium to scrape the top 10 Billboard song titles for a given chart URL.

        Args:
            search_url (str): The full URL to the Billboard chart page.

        Returns:
            List[str]: A list of up to 10 song titles.
        """
        print(search_url)

        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")

        service = Service(r"C:\Dane\998_selenium\chromedriver-win64\chromedriver.exe")
        driver = webdriver.Chrome(service=service, options=options)

        driver.get(search_url)
        time.sleep(3)

        page_html = driver.page_source
        driver.quit()

        soup = BeautifulSoup(page_html, "html.parser")
        ten_best_titles_list: List[str] = []

        titles = soup.select("li.o-chart-results-list__item h3.c-title")
        counter = 0

        for title in titles:
            text = title.get_text(strip=True)
            ten_best_titles_list.append(text)
            counter += 1
            if counter == 10:
                break

        print(ten_best_titles_list)
        return ten_best_titles_list


class SpotifySearcher:
    """
    Class responsible for searching song titles using the Spotify API.
    """

    def __init__(self, client_id: str, client_secret: str) -> None:
        """
        Initializes the Spotify API client using client credentials.

        Args:
            client_id (str): Spotify Client ID.
            client_secret (str): Spotify Client Secret.
        """
        auth = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        self.sp = spotipy.Spotify(auth_manager=auth)

    def search_and_print(self, titles: List[str]) -> None:
        """
        Searches Spotify for each title and prints the first match.

        Args:
            titles (List[str]): A list of song titles to search for.
        """
        for title in titles:
            try:
                result = self.sp.search(q=title, type="track", limit=1)
                items = result.get("tracks", {}).get("items", [])

                if items:
                    track = items[0]
                    name = track["name"]
                    artist = track["artists"][0]["name"]
                    url = track["external_urls"]["spotify"]
                    print(f"🎵 {name} – {artist}\n🔗 {url}\n")
                else:
                    print(f"Not found: {title}")
            except Exception as e:
                print(f"Error searching '{title}': {e}")


def main() -> None:
    """
    Main entry point for the program.
    Prompts user for date, scrapes Billboard, and searches Spotify.
    """
    my_search_date = MusicTimeVehicle.choose_srap_date()
    my_music = MusicTimeVehicle(my_search_date)
    search_url = my_music.build_url()
    print(f"Scraping from: {search_url}")
    song_titles = my_music.selenium_web_connector(search_url)

    searcher = SpotifySearcher(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET_ID)
    searcher.search_and_print(song_titles)


if __name__ == "__main__":
    main()