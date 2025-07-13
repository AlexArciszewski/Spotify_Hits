import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from typing import List


class SpotifySearcher:
    def __init__(self, client_id: str, client_secret: str) -> None:
        """
        Initialize the SpotifySearcher with Spotify API credentials.
        Args: client_id (str): Spotify API Client ID.
        client_secret (str): Spotify API Client Secret.
        """
        auth = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        self.sp = spotipy.Spotify(auth_manager=auth)

    def search_and_print(self, titles: List[str]) -> None:
        """
        Search Spotify for each title and print the first matching track info.
        Args:titles (List[str]): List of song titles to search for.
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
                    print(f"{name} – {artist}\n{url}\n")
                else:
                    print(f"Not found: {title}")
            except Exception as e:
                print(f"Error searching '{title}': {e}")