Spotify Hits Scraper

This Python project lets you fetch the top 10 songs from the Billboard Hot 100 chart for a specific date and search for them on Spotify using the Spotify API.

1. Features

   - Prompt the user for a date (format: YYYY-MM-DD)
   - Scrape Billboard’s Hot 100 chart for that date (top 10 only)
   - Search the scraped titles on Spotify
   - Display the results: track name, artist, and Spotify URL

2. Requirements

   - Python 3.10+
   - Spotify Developer credentials (Client ID and Client Secret)

3. Libraries Used

   - `selenium`
   - `beautifulsoup4`
   - `spotipy`
   - `python-dotenv`

4. Project Structure

   ├── main.py
   ├── billboard_scraper.py
   ├── spotify_searcher.py
   ├── .env
   ├── requirements.txt
   ├── README.md
   └── tests/
         ├── __init__.py
         └── test_billboard_scrapper.py
	

5. How to Run the Project

   a. Clone the repository:
 
       git clone https://github.com/YourUsername/Spotify_Hits.git

   b. Navigate to the project folder and (optionally) create a virtual environment:

       python -m venv .venv
       .venv\Scripts\activate # On Windows

   c. Install the required packages:

       pip install -r requirements.txt


   d. Create a `.env` file in the root directory and add your Spotify API credentials:

       CLIENT_ID=your_spotify_client_id
       CLIENT_SECRET_KEY=your_spotify_client_secret

   e. Run the program:

       python main.py

6. Example Output

   After entering a date like `2002-07-06`, the program will show the top 10 tracks from that day along with the artist names and Spotify links.

7. Notes

   - The script uses Selenium, so make sure you have ChromeDriver installed and set the correct path in `billboard_scraper.py`.
   - For simplicity and performance, the script only fetches the first 10 songs.
   - Do not commit your `.env` file or any sensitive credentials to GitHub — make sure `.env` is listed in `.gitignore`.

8. License

   This project is licensed under the MIT License.
