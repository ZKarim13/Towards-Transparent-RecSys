"""module doc string"""

import os
import zipfile


# rename this function to extract zip
def extract_dataset(source_path: str, destination_path: str, remove_zip=False):
    """Extracts a zip file to a specific destination

    Patameters:
    source_path (str):
    destination_path (str):
    remove_zip (bool):
    verbose (bool):

    Note:
    - if the destination_path does not exist, the function will create it automatically.

    Returns:
    - None

    Example:
    extract_zip()
    """

    # create the destination_path if it does not exist.
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)

    # Extract files from the zip archive
    with zipfile.ZipFile(source_path, "r") as zip_ref:
        zip_ref.extractall(destination_path)

    # if verbose:
    #    print(f"Dataset extracted to: {destination_path}")

    # Remove the zip file if specified
    if remove_zip:
        os.remove(source_path)
        # if verbose:
        #    print(f"Zip file removed: {source_path}")
