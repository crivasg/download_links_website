'''__main__.py'''

from download_links_website.cli import read_user_cli_args
from download_links_website.web_requests import request_json_url, download_file, parse_url
import os

def main():

    user_args = read_user_cli_args()
    url = user_args.url
    dest_folder =  user_args.dest_folder
    
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder, exist_ok=True)
    
    link_urls = parse_url(url)
    for link_url in link_urls:
        print(link_url)
        download_file(link_url, dest_folder=dest_folder)
    

if __name__ == '__main__':
    main()
