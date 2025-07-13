import sys
import os
import unittest

# Add parent directory to sys.path to import billboard_scraper module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from billboard_scraper import MusicTimeVehicle


class TestMusicTimeVehicle(unittest.TestCase):
    """
    Unit tests for the MusicTimeVehicle class.
    """

    def test_build_url_valid_date(self) -> None:
        """
        Test build_url returns correct URL when a valid date is provided.
        """
        # given
        vehicle = MusicTimeVehicle("2002-07-06")
        # when
        result = vehicle.build_url()
        # then
        expected_url = "https://www.billboard.com/charts/hot-1002002-07-06"
        self.assertEqual(result, expected_url)

    def test_build_url_empty_date(self) -> None:
        """
        Test build_url returns base URL when an empty date string is provided.
        """
        vehicle = MusicTimeVehicle("")
        result = vehicle.build_url()
        expected_url = "https://www.billboard.com/charts/hot-100"
        self.assertEqual(result, expected_url)


if __name__ == "__main__":
    unittest.main()