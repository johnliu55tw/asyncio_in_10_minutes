import sys
from base64 import b64encode

import requests


def get_token(client_id, client_secret):
    enc_auth = b64encode((client_id + ':' + client_secret).encode('ascii')).decode('ascii')
    resp = requests.post('https://account.kkbox.com/oauth2/token',
                         headers={'Authorization': 'Basic ' + enc_auth},
                         data={'grant_type': 'client_credentials'})
    if 'error' in resp.json():
        raise ValueError('Unable to retrive token with {} and {}: {}'.format(resp.json()['error']))
    else:
        return resp.json()


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: get_token.py CLIENT_ID CLIENT_SECRET')
        sys.exit(1)

    token = get_token(sys.argv[1], sys.argv[2])
    print(token['access_token'])
