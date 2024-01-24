import urllib.request
import argparse

def download_file(url:str, destination_path:str, verbose:bool):
    """Download a file from the internet and save it to the specified destination.

    Args:
        url (str): The URL of the file to be downloaded.
        destination_path (str): The path where the downloaded file should be saved.
        verbose(bool): print detailed progress information during the download.
    """
    def progress_callback(block_num, block_size, total_size):
        """Callback function to display download progress."""
        downloaded = block_num * block_size
        percent = (downloaded / total_size) * 100
        print(f"Downloaded: {downloaded}/{total_size} bytes ({percent:.2f}%)", end='\r')

    urllib.request.urlretrieve(url,
                               destination_path,
                               reporthook=progress_callback if verbose else None,
                               )
    if verbose:
        print("\nDownload complete.")
        print(f'downloaded to: {destination_path}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument('url')
    parser.add_argument('des')
    parser.add_argument('-v', '--verbose', action='store_true') 
    args = parser.parse_args()

    download_file(args.url, args.des, args.verbose)
