# Dependencies
import os
import requests as req
import validators as valid
from pathlib import Path
from zipfile import ZipFile

# Define Functions
def get_and_unpack_dataset(dataset_src_url, dataset_name):
    """
    Download a zip-archive dataset from an url and unpack it in the datasets directory.
    
    Arguments:
    - dataset_src_url <string>: Required. The url to the zip dataset.
    - dataset_name <string>: Required. The name for the dataset. This will be the folder that the dataset will be extracted into.
    """
    
    try:
        # Argument check
        assert type(dataset_src_url) == str and valid.url(dataset_src_url), "'dataset_src_url' argument is required and must be a valid url"
        assert type(dataset_name) == str and len(dataset_name) >= 3, "'dataset_name' argument is required and must be at least 3 characters"

        # Constants
        PROJ_DIR = Path().resolve().parent
        DATASETS_DIR = os.path.join(PROJ_DIR, "datasets")
        DATASETS_ZIP_DIR = os.path.join(DATASETS_DIR, "__archives__")

        # Create directories if needed
        if not os.path.isdir(DATASETS_DIR): 
            os.mkdir(DATASETS_DIR)
            
        if not os.path.isdir(DATASETS_ZIP_DIR): 
            os.mkdir(DATASETS_ZIP_DIR)

        # Dataset name and target directory
        dataset_name = dataset_name.replace(" ", "_").lower()
        dataset_target_dir = os.path.join(DATASETS_DIR, dataset_name)

        # Send the request
        res = req.get(dataset_src_url, stream=True)

        # Save the zip file
        with open(os.path.join(DATASETS_ZIP_DIR, f"{dataset_name}.zip"), "wb+") as f:
            for chunk in res.iter_content(chunk_size=512):
                if chunk:  # filter out keep-alive new chunk
                    f.write(chunk)

        # Unpack the zip file into its directory
        with ZipFile(os.path.join(DATASETS_ZIP_DIR, f"{dataset_name}.zip"), "r") as zip_obj:
            zip_obj.extractall(dataset_target_dir)
        
        return PROJ_DIR
    
    except Exception as e:
        return f"Error: {e}"