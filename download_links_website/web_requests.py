'''web_requests.py'''

import json
import os

import requests
from tqdm import tqdm
from bs4 import BeautifulSoup

from  urllib.parse import urlparse

def parse_url(url:str) -> list[str]:

    url_list = []

    page = requests.get(url)
    ##print('-'*80,page.text,'-'*80,page.headers['content-type'],sep='\n')


    contents= page.text
    
    soup = BeautifulSoup(contents, 'html.parser')
    print(f'{soup.title.name} : {soup.title.string}')

    links = soup.find_all('a')
    if len(links) == 0 :
        return []
    
    links = [ link for link in links if link.get('href').endswith('.pdf') ]

    for link in links:
        pdf_link = link.get('href')
        if not pdf_link in url_list:
            url_list.append(pdf_link)

    return url_list

def request_json_url(url:str) -> dict:
    '''returns the string of a URL'''

    data = {}
    r = requests.get(url, allow_redirects=True)
    status_code = r.status_code
    #print('status_code',r.status_code, sep=' = ')
    # check that the status code is not bad., if bad, returns empty dict
    if r.status_code != requests.codes.ok:
        return data
    status_code = r.status_code
    headers = r.headers
    content_type = r.headers.get('content-type')
    if content_type.lower() == 'application/json':
        data = r.json()

    return data


def download_file(url:str, dest_folder:str=None) -> str:
    ''' downloads a file to the local drive from an url with a progress bar thanks to 'tqdm'
Referenes:
 - https://stackoverflow.com/a/16696317
 - Progress Bar while download file over http with Requests: https://stackoverflow.com/a/37573701
'''

    chunk_size=8192
    
    temp_dir = os.environ.get('TEMP')
    if dest_folder:
        temp_dir = dest_folder

    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir, exist_ok=True)

    url_data = urlparse(url)
    filename = url_data.path.split('/')[-1]
    local_filename = os.path.join(temp_dir, filename)
    print(f'{url} -> {local_filename!s}')
        
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as resp:
        headers = resp.headers
        total_size_in_bytes= int(resp.headers.get('content-length', 0))
        ##print(f'{total_size_in_bytes=}')
        resp.raise_for_status()

        progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
        with open(local_filename, 'wb') as f:
            for chunk in resp.iter_content(chunk_size): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk:
                progress_bar.update(len(chunk))
                f.write(chunk)
        progress_bar.close()
        
    return local_filename
