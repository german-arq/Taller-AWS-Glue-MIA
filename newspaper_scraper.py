import boto3
from datetime import datetime
from urllib.request import urlopen

# Get current day
today = datetime.now().date()

# Config for saving file in s3
client = boto3.client("s3", "us-east-1")
bucket = "mia-e3-headlines-raw"
file_name = f"eltiempo-{today}.html"

# Newspaper's url
url = "https://www.eltiempo.com/"

# Open and save html of newspaper front page
with urlopen(url) as response:
    html_doc = response.read()

client.put_object(Bucket=bucket, Body=html_doc, Key=file_name)