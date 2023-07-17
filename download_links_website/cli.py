'''cli.py'''

import argparse
import pathlib
import os

def read_user_cli_args():
    '''Handle the CLI arguments and options'''
    
    parser = argparse.ArgumentParser(prog='download_links_website',
                                     description='Downloads the linked files from an URL')

    parser.add_argument('-u','--url',
                        type=str,
                        required=True,
                        help='Enter URL to parse')

    parser.add_argument('--dest_folder',
                        type=str,
                        default=os.environ.get('TEMP'),
                        required=False,
                        help='Destination folder')
                                     
    return parser.parse_args()
