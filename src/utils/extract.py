import os
import zipfile

def extract_dataset(source_path, destination_path, remove_zip=False, verbose=True):
    # Create the destination directory if it doesn't exist
    os.makedirs(destination_path, exist_ok=True)

    # Extract files from the zip archive
    with zipfile.ZipFile(source_path, 'r') as zip_ref:
        zip_ref.extractall(destination_path)

    if verbose:
        print(f"Dataset extracted to: {destination_path}")

    # Remove the zip file if specified
    if remove_zip:
        os.remove(source_path)
        if verbose:
            print(f"Zip file removed: {source_path}")

