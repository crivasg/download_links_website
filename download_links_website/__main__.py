'''__main__.py'''

from download_links_website.cli import read_user_cli_args
from download_links_website.web_requests import request_json_url, download_file, parse_url

from download_links_website.data import read_file 

import os
import re

def main():

    user_args = read_user_cli_args()
    url = user_args.input
    dest_folder =  user_args.dest_folder

    if url is None:
        return
    
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder, exist_ok=True)

    # detect if string is URL or a file
    if os.path.exists(os.path.normpath(url)):
        file_path = os.path.normpath(url)

        url_list = [ fn for fn in read_file(file_path) if re.match('^(http|https)://', fn) ]
        for link_url in url_list:
            print(f'-> {link_url}')
            download_file(link_url, dest_folder=dest_folder)
             
    else:
        print(url)
        link_urls = parse_url(url)
        #link_urls=[]
        for link_url in link_urls:
            download_file(link_url, dest_folder=dest_folder)
    

if __name__ == '__main__':
    main()
