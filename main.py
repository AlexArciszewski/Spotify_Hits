from dotenv import load_dotenv
import os
from typing import Optional

from billboard_scraper import MusicTimeVehicle
from spotify_searcher import SpotifySearcher

load_dotenv()

SPOTIFY_CLIENT_ID: Optional[str] = os.getenv("CLIENT_ID")
SPOTIFY_CLIENT_SECRET_ID: Optional[str] = os.getenv("CLIENT_SECRET_KEY")


def main() -> None:
    """
    Main entry point of the program:
    Prompts the user for a date, constructs the Billboard URL for that date,
    scrapes the top 10 song titles from the Billboard page,
    searches for these songs on Spotify and prints the results.
    """
    my_search_date = MusicTimeVehicle.choose_scrap_date()
    my_music = MusicTimeVehicle(my_search_date)
    search_url = my_music.build_url()
    print(f"Scraping from: {search_url}")
    song_titles = my_music.selenium_web_connector(search_url)

    searcher = SpotifySearcher(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET_ID)
    searcher.search_and_print(song_titles)


if __name__ == "__main__":
    main()