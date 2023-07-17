'''__main__.py'''

from download_links_website.cli import read_user_cli_args
from download_links_website.web_requests import request_json_url, download_file, parse_url


def main():
    user_args = read_user_cli_args()
    url = user_args.url
    dest_folder =  user_args.dest_folder
    print(url)
    print(dest_folder)
    #parse_url(url=url)
    
    link_urls = parse_url(url)
    print(f'{link_urls=}')
    

if __name__ == '__main__':
    main()
