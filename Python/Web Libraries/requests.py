import requests

import time

def download_site(url, session):
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")

url = "https://www.jython.org"

with requests.Session() as session:
    download_site(site, session)

# Read 10782 from https://www.jython.org

 with requests.Session() as session:
     start_time = time.time()
     download_site(site, session)
     duration = time.time() - start_time
     print(f"Downloaded in {duration} seconds")

# Read 10782 from https://www.jython.org
# Downloaded in 0.11608099937438965 seconds
