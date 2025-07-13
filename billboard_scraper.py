from typing import List
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

BILLBOARD_BASE_URL = "https://www.billboard.com/charts/hot-100"


class MusicTimeVehicle:
    def __init__(self, my_search_date: str) -> None:
        """
        Initialize MusicTimeVehicle with a specific date for the Billboard chart.
        Args:my_search_date (str): Date string formatted as '/YYYY-MM-DD/'.
        """
        self.my_search_date = my_search_date

    def build_url(self) -> str:
        """
        Construct the full Billboard chart URL for the given date.
        Returns:str: Complete URL to the Billboard Hot 100 chart for the date.
        """
        return f"{BILLBOARD_BASE_URL}{self.my_search_date}"

    @staticmethod
    def choose_scrap_date() -> str:
        """
        Prompt the user to enter a date string for scraping.
        Returns: str: User input date string in '/YYYY-MM-DD/' format.
        """
        return input("Please give me the date with format ->'/YYYY-MM-DD/': ")

    def selenium_web_connector(self, search_url: str) -> List[str]:
        """
        Use Selenium to fetch and parse the Billboard Hot 100 page,
        extracting the top 10 song titles.
        Args: search_url (str): URL of the Billboard Hot 100 chart to scrape.
        Returns: List[str]: List of top 10 song titles scraped from the page.
        """
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")

        service = Service(r"C:\Dane\998_selenium\chromedriver-win64\chromedriver.exe")
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(search_url)
        time.sleep(3)  # Wait for dynamic content to load

        page_html = driver.page_source
        driver.quit()

        soup = BeautifulSoup(page_html, "html.parser")
        top_ten_titles: List[str] = []
        titles = soup.select("li.o-chart-results-list__item h3.c-title")

        for count, title in enumerate(titles):
            text = title.get_text(strip=True)
            top_ten_titles.append(text)
            if count == 9:
                break

        return top_ten_titles

