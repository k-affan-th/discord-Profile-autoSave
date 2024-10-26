# %%
import requests

def download_image(url:str, filename):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an exception for error HTTP status codes

        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:  # Filter out keep-alive new chunks
                    f.write(chunk)

        return (f"Image downloaded successfully: {filename}")
    except Exception as e:
        return (f"Error downloading image: {e}")

# %%

import hashlib
import shutil
import os

def calculate_hash(file_path):
    """Calculates the SHA256 hash of a file."""
    with open(file_path, 'rb') as f:
        hash_obj = hashlib.sha256()
        while True:
            chunk = f.read(1024)
            if not chunk:
                break
            hash_obj.update(chunk)
        return hash_obj.hexdigest()
    
def check_for_duplicates_and_handle(downloaded_file:str, target_folder:str, debug=False) -> tuple[bool,str]:
    download_file_hash = calculate_hash(downloaded_file)
    return_string = ''
    for file_name in os.listdir(target_folder):
        file_path = os.path.join(target_folder, file_name)
        file_hash = calculate_hash(file_path)
        if download_file_hash == file_hash:
            return_string += f"    File '{file_name}' is a duplicate."
            os.remove(downloaded_file)  # Delete the temporary file
            # Report the user (implement your reporting mechanism here)
            return (False, return_string)
    
    # If no duplicates found, move the temp file to the correct folder
    shutil.move(downloaded_file, target_folder)
    
    return_string += "File moved successfully."
    return (True, return_string)