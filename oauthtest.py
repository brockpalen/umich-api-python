from pprint import pprint
import logging
from requests.auth import HTTPBasicAuth
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session


#grab client_id and client_secret from:
#https://api.it.umich.edu
client_id = u'<clientid>'
client_secret = u'<secret>'

token_url = 'https://api-gw.it.umich.edu/token'

basic_auth = HTTPBasicAuth(client_id, client_secret)

client = BackendApplicationClient(client_id=client_id, client_secret=client_secret)

oauth = OAuth2Session(client=client)

token = oauth.fetch_token(token_url=token_url,
                          auth=basic_auth)

r = oauth.get(u'https://api-gw.it.umich.edu/Mcommunity/People/v1/people/brockp',
              headers={'Accept':'application/json'})

pprint(r.json())
