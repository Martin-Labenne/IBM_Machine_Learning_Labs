import os
import requests

def get_filename_from_url(url):
    filename = os.path.basename(url)
    return filename


def save_file_if_not_exists(url, prefix=None, filename=None): 
    
    file_path = prefix + ( filename if filename else get_filename_from_url(url) )

    # Create the directories if they don't exist
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    if not os.path.exists(file_path):
        response = requests.get(url)
        with open(file_path, 'wb') as file:
            file.write(response.content)
        
    return file_path
