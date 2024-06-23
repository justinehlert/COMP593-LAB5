'''
Library for interacting with the PasteBin API
https://pastebin.com/doc_api
'''
import requests

PASTEBIN_API_POST_URL = 'https://pastebin.com/api/api_post.php'
API_DEV_KEY = 'ZuELwWDj92E5MHtAT5LXcMAccQU0yNlB'


def post_new_paste(title, body_text, expiration='N', listed=True):
    """Posts a new paste to PasteBin

    Args:
        title (str): Paste title
        body_text (str): Paste body text
        expiration (str): Expiration date of paste (N = never, 10M = minutes, 1H, 1D, 1W, 2W, 1M, 6M, 1Y)
        listed (bool): Whether paste is publicly listed (True) or not (False) 
    
    Returns:
        str: URL of new paste, if successful. Otherwise None.
    """    
    # TODO: Function body
    # Note: This function will be written as a group 
    payload = {'api_dev_key': API_DEV_KEY, 'api_option': 'paste', 'api_paste_code': body_text}
    r = requests.post(PASTEBIN_API_POST_URL, data=payload)
    pastebinurl = r.text
    return pastebinurl
