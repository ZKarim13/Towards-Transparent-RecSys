"""
Download Module

This module provides utility functions for downloading files from the internet.
"""

import os
import urllib.request


def download_file(url: str, destination_path: str):
    """Download a file from the internet and save it to the specified destination.

    Parameters:
    - url (str): The URL of the file to be downloaded.
    - destination_path (str): The path where the downloaded file should be saved.

    Note:
    - if the destination_path does not exist, the function will create it automatically.

    Returns:
    - None

    Raises:
    - ValueError: If the provided URL is invalid or if there are issues during the download.

    Example:
    - download_file('https://example.com/file.zip', '/path/to/destination', True)
    """

    def progress_callback(block_num, block_size, total_size):
        """Callback function to log the download progress."""
        downloaded = block_num * block_size
        percent = int((downloaded / total_size) * 100)
        if percent % 10 == 0:
            print("Downloaded: %i/%i bytes (%i%%)" % (block_num, block_size, percent))

    # create the destination_path if it does not exist.
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)

    urllib.request.urlretrieve(url, destination_path, reporthook=progress_callback)
