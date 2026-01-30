import functions_framework
import pandas as pd
from google.cloud import bigquery

@functions_framework.cloud_event
def handle_cricket_data(cloud_event):
    # This code runs whenever a file is uploaded to GCS
    data = cloud_event.data
    file_name = data["name"]
    bucket_name = data["bucket"]

    print(f"New cricket file detected: {file_name} in {bucket_name}")
    
    # We will add your ICC filtering logic here next!